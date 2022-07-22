# wrapper-gcode-ci
CI for generating Wrapper G-code

## How this works?

- Any changes to `.py` and `.yml` files will trigger [GitHub Actions](https://github.com/singh-ramanpreet/wrapper-gcode-ci/actions).
- Python script `generate.py` using `config.yml` will generate G-Code for different tile sizes.
- Generated G-Code will be committed to this `main` branch by [GitHub Actions](https://github.com/singh-ramanpreet/wrapper-gcode-ci/actions), if there are changes.

## How to download generated G-Code?

Use PowerShell script `download-gcode.ps1` to download `R*.PIT` files to PC connected to machine.`

1. Get the PS Script. Right-Click [download](https://raw.githubusercontent.com/singh-ramanpreet/wrapper-gcode-ci/main/download-gcode.ps1)
 link and select `Save As`. 
2. Run the Script. Right-Click the downloaded script, select `Run With PowerShell`. Select the destination folder and press `Ok`.

