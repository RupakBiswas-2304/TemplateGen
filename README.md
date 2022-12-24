# Template Generator:

## Usage
Use this for generating a file on some template.
Before start using please change the please mention your template folder path in the `config.py` file.

For adding template in your template file, use the `template` extension. For example `py1.template` is a template file.

## Commands :
- For listing all templates use `-l` flag.
```bash
templategen -l
```
- For generating a file from a template use `-t` flag for template name then the file name. for example:
```bash
templategen -t py1 test.py
```
- For adding a template use `-a` flag for template name then the file name. for example:
```bash
templategen -a py1 test.py
```
- The above command create a template named `py1.template` in your template folder with `test.py` content.

- Saving a directory as a template ->
```
templategen -ad directory_name
```
- This will save that whole directory as a template. If you want to add some dynamic naming, you can use `{{variable name}}` in `config.json` file, also create a `replace.json` file with the given format in demo template folder.

- For using a template as a directory ->
```
templategen -d directory_name
```

- Use `--help` for help.
```bash
templategen --help
```

## Installation :
```bash
chmod +x main.py
sudo ln -s (pwd)/main.py /usr/bin/templategen
```
- This works for both `fish` and `bash` shell.
