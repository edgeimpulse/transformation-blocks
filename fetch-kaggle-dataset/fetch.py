import os, sys, argparse, pathlib
import shutil

# Set the arguments
parser = argparse.ArgumentParser(description='Organization transformation block')
parser.add_argument('--kaggle_dataset', type=str, required=True, help="username/dataset")
parser.add_argument('--bucket_name', type=str, required=True, help="Bucket to store the dataset")
parser.add_argument('--bucket_directory', type=str, required=False, help="Bucket prefix to store the dataset")

args, unknown = parser.parse_known_args()
dataset = args.kaggle_dataset
bucket_name = args.bucket_name
bucket_prefix = args.bucket_directory
mount_prefix = os.getenv('MOUNT_PREFIX', '/mnt/s3fs/')

out_folder = os.path.join(mount_prefix, bucket_name, bucket_prefix) if bucket_prefix else os.path.join(mount_prefix, bucket_name)
print('out_folder', out_folder, flush=True)

# create the output directory if needed
pathlib.Path(out_folder).mkdir(parents=True, exist_ok=True)

if not os.getenv('KAGGLE_USERNAME'):
    print('Missing KAGGLE_USERNAME', flush=True)
    sys.exit(1)

if not os.getenv('KAGGLE_KEY'):
    print('Missing KAGGLE_KEY', flush=True)
    sys.exit(1)

print("Downloading dataset... " + dataset, flush=True)
os.system('kaggle datasets download --force -d ' + dataset)

dataset = args.kaggle_dataset.split('/')[1]

print("Extracting dataset "+dataset+".zip to "+out_folder+"/ directory", flush=True)
shutil.unpack_archive(dataset+'.zip', out_folder)

print("Finished")
sys.exit(0)

