import os, sys, argparse, shutil
import pandas as pd
import matplotlib.pyplot as plt

# Set the arguments
parser = argparse.ArgumentParser(description='Organization transformation block')
parser.add_argument('--bucket_name', type=str, required=False, help="Bucket where your dataset is hosted")
parser.add_argument('--bucket_directory', type=str, required=False, help="Directory in your bucket where your dataset is hosted")
parser.add_argument('--in-directory', type=str, required=False, help="Argument passed by Edge Impulse transformation block when the --in-directory option is selected")
parser.add_argument('--out-directory', type=str, required=False, help="Argument passed by Edge Impulse transformation block when the --out-directory option is selected")
parser.add_argument('--in-file', type=str, required=False, help="Argument passed by Edge Impulse transformation block when the --in-file option is selected")
parser.add_argument('--file_name', type=str, required=False, help="Filename + extension that needs to be copied to the output directory")

args, unknown = parser.parse_known_args()


print('--bucket_name: ', args.bucket_name, flush=True)
print('--bucket_directory: ', args.bucket_directory, flush=True)
print('--in-directory: ', args.in_directory, flush=True)
print('--out-directory: ', args.out_directory, flush=True)
print('--in-file: ', args.in_file, flush=True)
print('--file_name: ', args.file_name, flush=True)


if args.out_directory:
    # verify that the output directory exists and display content
    if not os.path.exists(args.out_directory):
        print('--out-directory argument', args.out_directory, 'does not exist', flush=True)
    else:
        print('out-directory has', os.listdir(args.out_directory), flush=True)

    # verify that the input directory exists and display content
    if args.in_directory:
        if not os.path.exists(args.in_directory):
            print('--in-directory argument', args.in_directory, 'does not exist', flush=True)
        else:
            print('in-directory has', os.listdir(args.in_directory), flush=True)
            # verify if file_name exists in input directory and copy it to output directory
            if os.path.exists(os.path.join(args.in_directory, args.file_name)):
                shutil.copyfile(os.path.join(args.in_directory, args.file_name), os.path.join(args.out_directory, args.file_name))
                print('Copying file from ', args.in_directory, 'to ', args.out_directory)
                print('out-directory has now', os.listdir(args.out_directory), flush=True)

    # verify that the input file exists
    if args.in_file:
        if not os.path.exists(args.in_file):
            print('--in-file argument', args.in_file, 'does not exist', flush=True)
        else:
            print('--in-file path', args.in_file, 'exist', flush=True)
            print("filename: ", os.path.basename(args.in_file))
            # copy input file to output directory
            shutil.copyfile(os.path.join(args.in_file), os.path.join(args.out_directory, os.path.basename(args.in_file)))
            print('out-directory has now', os.listdir(args.out_directory), flush=True)

 # check if bucket name is set       
if args.bucket_name:
    bucket_dir = os.path.join('/mnt/s3fs/', args.bucket_name, args.bucket_directory) if args.bucket_directory else os.path.join('/mnt/s3fs/', args.bucket_name)
    # verify bucket directory is accessible and display content
    if not os.path.exists(bucket_dir):
        print('bucker_dir ', bucket_dir, 'does not exist', flush=True)
    else:
        print('bucket_dir has', os.listdir(bucket_dir), flush=True)


print("Finished")
sys.exit(0)

