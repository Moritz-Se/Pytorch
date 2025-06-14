# -*- coding: utf-8 -*-
"""integrate_data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_l3asGL1YZjF8LfoFKCdMtQqD24NgUIT
"""

import torch
from torchvision import datasets
import requests
import zipfile
from pathlib import Path


def integrate_picture_classification_data(image_folder: str,      #Name of the package the data is called
                                          url: str,                       #Url for downloading
                                          data_path: str="data/",               #Saved under data but can be changed
                                          force_redownload: bool = False
                                          ) -> str:

  data_path = Path(data_path)

 #set image_path. Could be used in later code --> gets returned!
  image_path = data_path / image_folder

#Create folders if not existing
  if image_path.is_dir():
    if force_redownload == True:
      print(f"{image_path} directory already exists but redownload is forced")
      image_path.rmdir(parents=True, exist_ok=True)
      image_path.mkdir(parents=True, exist_ok=True)
    elif force_redownload == False:
      print(f"{image_path} directory already exists")

  else:
    print(f"Creating {image_path} directory")
    image_path.mkdir(parents=True, exist_ok=True)

  with open(data_path / "Clustore.zip", "wb") as f:
    request = request.get(url)
    print(f"Downloading {url} to {image_path}...")
    f.write(request.content)

  with zipfile.ZipFile(data_path / "pizza_steak_sushi.zip", "r") as zip_ref:
    print(f"Unzipping {image_folder} data...")
    zip_ref.extractall(image_path)

  return image_path

