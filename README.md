# Pixel Art Rose Generator

![](https://img.shields.io/github/stars/Nitnaf10/Pixel-Art-Rose-Generator?style=flat-square)
![](https://img.shields.io/github/forks/Nitnaf10/Pixel-Art-Rose-Generator?style=flat-square)
![](https://img.shields.io/github/watchers/Nitnaf10/Pixel-Art-Rose-Generator?style=flat-square)
![](https://img.shields.io/github/contributors/Nitnaf10/Pixel-Art-Rose-Generator?style=flat-square)
![](https://img.shields.io/github/commit-activity/m/Nitnaf10/Pixel-Art-Rose-Generator?style=flat-square)
![](https://img.shields.io/github/last-commit/Nitnaf10/Pixel-Art-Rose-Generator?style=flat-square)
![](https://img.shields.io/github/languages/count/Nitnaf10/Pixel-Art-Rose-Generator?style=flat-square)
![](https://img.shields.io/github/languages/top/Nitnaf10/Pixel-Art-Rose-Generator?style=flat-square)

An algorithmic generator of symmetrical patterns inspired by rosettes, developed in Python.

---

## Example
<table>
  <tr>
    <td><img src="https://raw.githubusercontent.com/Nitnaf10/Pixel-Art-Rose-Generator/main/generated/01.png" width="180" /></td>
    <td><img src="https://raw.githubusercontent.com/Nitnaf10/Pixel-Art-Rose-Generator/main/generated/02.png" width="180" /></td>
    <td><img src="https://raw.githubusercontent.com/Nitnaf10/Pixel-Art-Rose-Generator/main/generated/03.png" width="180" /></td>
    <td><img src="https://raw.githubusercontent.com/Nitnaf10/Pixel-Art-Rose-Generator/main/generated/04.png" width="180" /></td>
    <td><img src="https://raw.githubusercontent.com/Nitnaf10/Pixel-Art-Rose-Generator/main/generated/05.png" width="180" /></td>
  </tr>
  <tr>
    <td><img src="https://raw.githubusercontent.com/Nitnaf10/Pixel-Art-Rose-Generator/main/generated/06.png" width="180" /></td>
    <td><img src="https://raw.githubusercontent.com/Nitnaf10/Pixel-Art-Rose-Generator/main/generated/07.png" width="180" /></td>
    <td><img src="https://raw.githubusercontent.com/Nitnaf10/Pixel-Art-Rose-Generator/main/generated/08.png" width="180" /></td>
    <td><img src="https://raw.githubusercontent.com/Nitnaf10/Pixel-Art-Rose-Generator/main/generated/09.png" width="180" /></td>
    <td><img src="https://raw.githubusercontent.com/Nitnaf10/Pixel-Art-Rose-Generator/main/generated/10.png" width="180" /></td>
  </tr>
  <tr>
    <td><img src="https://raw.githubusercontent.com/Nitnaf10/Pixel-Art-Rose-Generator/main/generated/11.png" width="180" /></td>
    <td><img src="https://raw.githubusercontent.com/Nitnaf10/Pixel-Art-Rose-Generator/main/generated/12.png" width="180" /></td>
    <td><img src="https://raw.githubusercontent.com/Nitnaf10/Pixel-Art-Rose-Generator/main/generated/13.png" width="180" /></td>
    <td><img src="https://raw.githubusercontent.com/Nitnaf10/Pixel-Art-Rose-Generator/main/generated/14.png" width="180" /></td>
    <td><img src="https://raw.githubusercontent.com/Nitnaf10/Pixel-Art-Rose-Generator/main/generated/15.png" width="180" /></td>
  </tr>
  <tr>
    <td><img src="https://raw.githubusercontent.com/Nitnaf10/Pixel-Art-Rose-Generator/main/generated/16.png" width="180" /></td>
    <td><img src="https://raw.githubusercontent.com/Nitnaf10/Pixel-Art-Rose-Generator/main/generated/17.png" width="180" /></td>
    <td><img src="https://raw.githubusercontent.com/Nitnaf10/Pixel-Art-Rose-Generator/main/generated/18.png" width="180" /></td>
    <td><img src="https://raw.githubusercontent.com/Nitnaf10/Pixel-Art-Rose-Generator/main/generated/19.png" width="180" /></td>
    <td><img src="https://raw.githubusercontent.com/Nitnaf10/Pixel-Art-Rose-Generator/main/generated/20.png" width="180" /></td>
  </tr>
</table>

---

## Features

· Generation of patterns with 8-fold symmetry
· Random walk algorithm for organic variations
· Command-line interface
· Metadata (seed, steps) embedded in PNG files
· Customizable parameters: seed, size, number of steps

---

## Usage

```bash
# Automatic generation
python main.py save my_image

# Custom parameters
python main.py save my_image --seed 251515 --size 7 --step 1024

# Reading metadata
python main.py read my_image

# Help
python main.py help
```

## Options

|Option | Description|
|---|----|
|name   | File name *(required)*|
|--seed | Random seed *(auto by default)*|
|--size | Pattern size *(auto by default)*|
|--step | Number of steps *(auto by default)*|

---

## License

Open-source project—see the repository for terms of use.

Translated with DeepL.com (free version)