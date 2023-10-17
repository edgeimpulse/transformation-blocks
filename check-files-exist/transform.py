import os
import sys
import argparse
import json

def save_metadata(metadata, out_directory):
    all_ok = all(metadata['metadata'][m] != 0 for m in metadata['metadata'])
    metadata['metadata']['ei_check'] = 1 if all_ok else 0
    with open(os.path.join(out_directory, 'ei-metadata.json'), 'w') as f:
        json.dump(metadata, f, indent=4)
    exit(0)

def check_files_presence(directory, files, out_directory, existing_metadata):
    
    metadata = {
        "version": 1,
        "action": "add",
        "metadata": existing_metadata if existing_metadata else {}
    }

    missing_files = [file for file in files if not os.path.exists(os.path.join(directory, file))]
    
    if missing_files:
        metadata['metadata']['ei_check_files_present'] = 0
    else:
        metadata['metadata']['ei_check_files_present'] = 1


    save_metadata(metadata, out_directory)

def main():
    parser = argparse.ArgumentParser(description='Check if files are present and create directory-level metadata')
    parser.add_argument('--in-directory', type=str, required=True, help="Input directory where your files are located")
    parser.add_argument('--out-directory', type=str, required=False, help="Output directory")
    parser.add_argument('--files', type=str, required=True, help="File names to check, separated by commas")
    parser.add_argument('--metadata', type=json.loads, required=False, help="Existing metadata")

    args, _ = parser.parse_known_args()

    if not os.path.exists(args.in_directory):
        print('--in-directory argument', args.in_directory, 'does not exist', flush=True)
        sys.exit(1)

    existing_metadata = args.metadata if args.metadata else {}

    files_to_check = args.files.replace(' ', '').split(',')

    check_files_presence(args.in_directory, files_to_check, args.out_directory, existing_metadata)

if __name__ == "__main__":
    main()