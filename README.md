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
<div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr 1fr; grid-template-rows: 1fr 1fr 1fr 1fr; grid-gap: 10px; margin: 20px;">
  <!--01-20-->
  <img src="https://github.com/Nitnaf10/Pixel-Art-Rose-Generator/blob/main/generated/01.png?raw=true" alt="rosette_1" style="width: 100%;">
  <img src="https://github.com/Nitnaf10/Pixel-Art-Rose-Generator/blob/main/generated/02.png?raw=true" alt="rosette_2" style="width: 100%;">
  <img src="https://github.com/Nitnaf10/Pixel-Art-Rose-Generator/blob/main/generated/03.png?raw=true" alt="rosette_3" style="width: 100%;">
  <img src="https://github.com/Nitnaf10/Pixel-Art-Rose-Generator/blob/main/generated/04.png?raw=true" alt="rosette_4" style="width: 100%;">
  <img src="https://github.com/Nitnaf10/Pixel-Art-Rose-Generator/blob/main/generated/05.png?raw=true" alt="rosette_5" style="width: 100%;">
  <img src="https://github.com/Nitnaf10/Pixel-Art-Rose-Generator/blob/main/generated/06.png?raw=true" alt="rosette_6" style="width: 100%;">
  <img src="https://github.com/Nitnaf10/Pixel-Art-Rose-Generator/blob/main/generated/07.png?raw=true" alt="rosette_7" style="width: 100%;">
  <img src="https://github.com/Nitnaf10/Pixel-Art-Rose-Generator/blob/main/generated/08.png?raw=true" alt="rosette_8" style="width: 100%;">
  <img src="https://github.com/Nitnaf10/Pixel-Art-Rose-Generator/blob/main/generated/09.png?raw=true" alt="rosette_9" style="width: 100%;">
  <img src="https://github.com/Nitnaf10/Pixel-Art-Rose-Generator/blob/main/generated/10.png?raw=true" alt="rosette_10" style="width: 100%;">
  <img src="https://github.com/Nitnaf10/Pixel-Art-Rose-Generator/blob/main/generated/11.png?raw=true" alt="rosette_11" style="width: 100%;">
  <img src="https://github.com/Nitnaf10/Pixel-Art-Rose-Generator/blob/main/generated/12.png?raw=true" alt="rosette_12" style="width: 100%;">
  <img src="https://github.com/Nitnaf10/Pixel-Art-Rose-Generator/blob/main/generated/13.png?raw=true" alt="rosette_13" style="width: 100%;">
  <img src="https://github.com/Nitnaf10/Pixel-Art-Rose-Generator/blob/main/generated/14.png?raw=true" alt="rosette_14" style="width: 100%;">
  <img src="https://github.com/Nitnaf10/Pixel-Art-Rose-Generator/blob/main/generated/15.png?raw=true" alt="rosette_15" style="width: 100%;">
  <img src="https://github.com/Nitnaf10/Pixel-Art-Rose-Generator/blob/main/generated/16.png?raw=true" alt="rosette_16" style="width: 100%;">
  <img src="https://github.com/Nitnaf10/Pixel-Art-Rose-Generator/blob/main/generated/17.png?raw=true" alt="rosette_17" style="width: 100%;">
  <img src="https://github.com/Nitnaf10/Pixel-Art-Rose-Generator/blob/main/generated/17.png?raw=true" alt="rosette_18" style="width: 100%;">
  <img src="https://github.com/Nitnaf10/Pixel-Art-Rose-Generator/blob/main/generated/19.png?raw=true" alt="rosette_19" style="width: 100%;">
  <img src="https://github.com/Nitnaf10/Pixel-Art-Rose-Generator/blob/main/generated/20.png?raw=true" alt="rosette_20" style="width: 100%;">
</div>

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