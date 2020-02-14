from utils import create_input_files
import os

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='flickr8k',
                       karpathy_json_path=os.path.join("..", "caption_datasets","dataset_flickr8k.json"),#'caption_datasets/dataset_flicker8k.json',
                       image_folder=os.path.join("..","Flicker8k_Dataset"),#'Flicker8k_Dataset/Flicker8k_Dataset/',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder=os.path.join("..","Flicker8k_Dataset"),
                       max_len=50)
