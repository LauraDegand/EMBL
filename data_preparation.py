import os 
import numpy as np
from glob import glob
from tqdm import tqdm
import imageio
import tifffile
import argparse
from skimage.transform import rescale


def rescale_volume(im_path , target_shape , im_resc_folder):
	vol = imageio.volread(im_path)
	vol = resize(vol , target_shape)
	#vol = rescale(vol , scale=scale_factor , preserve_range=True)
	im_name = os.path.split(im_path)[1]
	imageio.volwrite(os.path.join(im_resc_folder , im_name) , vol)


def rescale_data(input_folder , list_paths):
	output_folder = os.path.join(input_folder , 'rescaled')
	im_resc_folder = os.path.join(output_folder , 'images')
	os.makedirs(im_resc_folder , exist_ok=True)
	target_shape = (128 , 128 , 128)
	for im_path in tqdm(list_paths):
		rescale_volume(im_path , target_shape , im_resc_folder)


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i' , '--input' , required=True)
	parser.add_argument('-list' , required=True)
	args = parser.parse_args()

	rescale_data(args.input , args.list )


if __name__ == "__main__":
	main()