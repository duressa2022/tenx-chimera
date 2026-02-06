# CI checks script for local validation of workflow steps
$required = @('specs','skills','tests','mcp')
$missingRequired = @()
foreach ($d in $required) {
    if (-not (Test-Path $d -PathType Container)) {
        $missingRequired += $d
    }
}
if ($missingRequired.Count -gt 0) {
    Write-Error "Missing required directories: $($missingRequired -join ', ')"
    exit 1
}
Write-Output "All required directories present"

# Verify each skill has a contract.json
$skills = Get-ChildItem -Path .\skills -Directory -ErrorAction SilentlyContinue
$missingContracts = @()
foreach ($s in $skills) {
    if (-not (Test-Path (Join-Path $s.FullName 'contract.json'))) {
        $missingContracts += $s.Name
    }
}
if ($missingContracts.Count -gt 0) {
    Write-Error "Missing contract.json in: $($missingContracts -join ', ')"
    exit 1
}
Write-Output "All skills have contract.json"

# Verify spec_reference exists in either contract.json or README.md for each skill
 $missing = @()
foreach ($s in $skills) {
    $has = $false
    $cj = Join-Path $s.FullName 'contract.json'
    $rm = Join-Path $s.FullName 'README.md'
    if (Test-Path $cj) {
        $text = Get-Content $cj -Raw -ErrorAction SilentlyContinue
        if ($text -match '"spec_reference"') { $has = $true }
    }
    if ((-not $has) -and (Test-Path $rm)) {
        $text2 = Get-Content $rm -Raw -ErrorAction SilentlyContinue
        if ($text2 -match 'spec_reference') { $has = $true }
    }
    if (-not $has) {
        $missing += $s.Name
    }
}
if ($missing.Count -gt 0) {
    Write-Error "Some skills missing spec_reference: $($missing -join ', ')"
    exit 1
} else {
    Write-Output 'All skills reference specs'
}

# Run tests: prefer pytest, fallback to Makefile (search recursively)
$pytestCmd = Get-Command pytest -ErrorAction SilentlyContinue
if ($pytestCmd) {
    Write-Output 'pytest found - running pytest -q'
    pytest -q
} else {
    $makefile = Get-ChildItem -Path . -Recurse -Filter Makefile -File -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($makefile) {
        Write-Output "Makefile found at $($makefile.FullName) - running make test"
        pushd $makefile.DirectoryName
        make test
        popd
    } else {
        $python = Get-Command python -ErrorAction SilentlyContinue
        if ($python) {
            Write-Output 'No pytest binary found, running python -m pytest -q'
            python -m pytest -q
        } else {
            Write-Output 'No test runner found - skipping tests'
        }
    }
}

# List implementation files
 $impl = Get-ChildItem -Path . -Recurse -Include *.py,*.ts,*.go -File -ErrorAction SilentlyContinue | Where-Object { $_.FullName -notmatch '\\venv\\|\\.venv\\|\\node_modules\\' }
if ($impl) {
    Write-Output 'Implementation files detected:'
    $impl | Select-Object -ExpandProperty FullName
} else {
    Write-Output 'No implementation files found.'
}
