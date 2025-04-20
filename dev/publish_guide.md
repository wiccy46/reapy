# Dependencies

- build
- twine

## Build

`python -m build`

## Publish

- Test Pypi: `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`
- Public: `twine upload dist/*`