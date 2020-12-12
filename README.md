# Filexts
Filexts is a module for working on file extension searching.

It searchs the file extension in a number of given directory, with much respect to android,
and return a list containing all filenames ending in that particular file extension.

The name filexts comes from **fil**e **ext**ension **s**earching

## API
`filexts.Filexts(filename, search_depth)`

Dependency: `glob.glob(filename)`
* **Filename**: is a string defining the file path in wild card.
* **Search_depth**: is an integer describing the number of directories to search through.

## Author
Jacob Mugala

# Licenses
