import os
import sys
import argparse
import pandas as pd
import json

def save_metadata(metadata, out_directory):
    all_ok = all(metadata['metadata'][m] != 0 for m in metadata['metadata'])
    metadata['metadata']['ei_check'] = 1 if all_ok else 0
    with open(os.path.join(out_directory, 'ei-metadata.json'), 'w') as f:
        json.dump(metadata, f, indent=4)
    exit(0)

def main():
    parser = argparse.ArgumentParser(description='Organization transformation block')
    parser.add_argument('--in-directory', type=str, required=True, help="Input directory where your files are located")
    parser.add_argument('--out-directory', type=str, required=False, help="Output directory")
    parser.add_argument('--files', type=str, required=True, help="CSV files, separated by commas")
    parser.add_argument('--key', type=str, required=True, help="Key to use to merge the CSV files")
    parser.add_argument('--join', type=str, required=True, help="Join method")
    parser.add_argument('--rename', type=str, required=True, help="By default, the first word of the folder will be used")
    parser.add_argument('--filename', type=str, required=False, help="Output filename (without extension)")
    parser.add_argument('--keep_all', type=str, required=False, help="Yes if keep all columns, no to select which columns to keep")
    parser.add_argument('--columns', type=str, required=False, help="Columns to keep, separated by commas")
    parser.add_argument('--metadata', type=json.loads, required=False, help="Existing metadata")

    args, unknown = parser.parse_known_args()
    print('--in-directory:', args.in_directory, flush=True)
    print('--out-directory:', args.out_directory, flush=True)
    print('--files:', args.files, flush=True)
    print('--key:', args.key, flush=True)
    print('--join:', args.join, flush=True)
    print('--rename:', args.rename, flush=True)
    print('--keep_all:', args.keep_all, flush=True)
    print('--columns:', args.columns, flush=True)
    print('--metadata:', args.metadata, flush=True)

    metadata = {
        "version": 1,
        "action": "replace",
        "metadata": args.metadata if args.metadata else {}
    }

    csv_files = args.files.replace(' ', '').split(',')
    merged_data = None

    if args.rename in ("True", "true", "1"):
        output_name = str(args.filename) + '.csv'
    else:
        path_components = os.path.normpath(args.in_directory).split(os.path.sep)
        last_directory = path_components[-1]
        output_name = str(last_directory.split('-')[0]) + '.merged.csv'

    print('output name:', str(output_name), flush=True)

    if args.out_directory:
        if not os.path.exists(args.out_directory):
            print('--out-directory argument', args.out_directory, 'does not exist', flush=True)
            metadata['metadata']['ei_check_files_merged'] = 0 
            save_metadata(metadata, args.out_directory)
        else:
            print('out-directory has', os.listdir(args.out_directory), flush=True)

        if args.in_directory:
            if not os.path.exists(args.in_directory):
                print('--in-directory argument', args.in_directory, 'does not exist', flush=True)
                metadata['metadata']['ei_check_files_merged'] = 0
                save_metadata(metadata, args.out_directory)
            else:
                print('in-directory has', os.listdir(args.in_directory), flush=True)
                for csv_file in csv_files:
                    if not os.path.exists(os.path.join(args.in_directory, csv_file)):
                        print('CSV file', csv_file, 'does not exist')
                        metadata['metadata']['ei_check_files_merged'] = 0
                        save_metadata(metadata, args.out_directory)
                    else:
                        print('CSV file', csv_file, 'exists')
                        if not csv_file.endswith('.csv'):
                            print(csv_file, 'has no .csv extension')
                            metadata['metadata']['ei_check_files_merged'] = 0
                            save_metadata(metadata, args.out_directory)
                        else:
                            df = pd.read_csv(os.path.join(args.in_directory, csv_file))

                            if args.keep_all not in ("True", "true", "1"):
                                print("removing columns")
                                columns_to_keep = args.columns.replace(' ', '').split(',')
                                columns_to_keep = [col.strip() for col in columns_to_keep]

                                # Remove columns that do not exist in the DataFrame
                                columns_to_keep = [col for col in columns_to_keep if col in df.columns]

                                if args.key not in columns_to_keep:
                                    columns_to_keep = [args.key] + columns_to_keep

                                df = df[columns_to_keep]

                                file_name = os.path.splitext(csv_file)[0]
                                suffix = f'_{file_name}'
                                columns_to_rename = {col: f'{col}{suffix}' for col in df.columns if col != args.key}
                                df = df.rename(columns=columns_to_rename)

                            if merged_data is None:
                                merged_data = df
                            else:
                                merged_data = pd.merge(merged_data, df, on=args.key, how=args.join, suffixes=('', f'_{os.path.splitext(csv_file)[0]}'))

                merged_data = merged_data.sort_values(by=args.key)
                merged_data.to_csv(os.path.join(args.out_directory, output_name), index=False)
                metadata['metadata']['ei_check_files_merged'] = 1
                save_metadata(metadata, args.out_directory)
                print('out-directory has now', os.listdir(args.out_directory), flush=True)
    else:
        print('Missing argument --out-directory does not exist')
        metadata['metadata']['ei_check_files_merged'] = 0
        save_metadata(metadata, args.out_directory)

    sys.exit(0)

if __name__ == "__main__":
    main()