## Setting up a dev environment

```bash
git clone <url>
cd pdfmerge
python -m .venv --prompt pdfmerge
source .venv/bin/activate
pip install -e ".[dev]"

pnpm install -g cspell
```

## Making a release

```bash
git checkout prod
git merge --no-ff --no-edit main
# update __init__.py version
# update changelog.md
pdm all

git commit -m "release: $VER"
git tag "$VER"
git push
git push --tags

git checkout main
git merge --no-ff --no-edit prod
git push
```
