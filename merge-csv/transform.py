import os, sys, argparse, shutil
import pandas as pd
import numpy as np

# Set the arguments
parser = argparse.ArgumentParser(description='Organization transformation block')
parser.add_argument('--in-directory', type=str, required=True, help="Input directory where your files are located")
parser.add_argument('--out-directory', type=str, required=False, help="Argument passed by Edge Impulse transformation block when the --out-directory option is selected")
parser.add_argument('--files', type=str, required=True, help="CSV files, separated by comas")
parser.add_argument('--key', type=str, required=True, help="Key to use to merge the CSV files")
parser.add_argument('--join', type=str, required=True, help="Join method")
parser.add_argument('--rename', type=str, required=True, help="By default, the first word of the folder will be used")
parser.add_argument('--filename', type=str, required=False, help="Output filename (without extension)")

args, unknown = parser.parse_known_args()
print('--in_directory: ', args.in_directory, flush=True)
print('--out_directory: ', args.out_directory, flush=True)
print('--files: ', args.files, flush=True)
print('--key: ', args.key, flush=True)
print('--join: ', args.join, flush=True)
print('--rename: ', args.rename, flush=True)


csv_files = args.files.replace(' ', '').split(',') # comma between keys
merged_data = None

# Output filename
if args.rename == True:
    output_name = str(args.filename) + '.csv'
else:
    # Normalize the path and split it into components
    path_components = os.path.normpath(args.in_directory).split(os.path.sep)
    # Get the last directory
    last_directory = path_components[-1]
    # Split the last directory by '-' to extract the first word
    output_name = str(last_directory.split('-')[0]) + '.merged.csv'
    
print('output name: ', str(output_name), flush=True)

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
            sys.exit(1)
        else:
            print('in-directory has', os.listdir(args.in_directory), flush=True)
            # verify if file_name exists in input directory and copy it to output directory
            for csv_file in csv_files:
                if not os.path.exists(os.path.join(args.in_directory, csv_file)):
                    print('CSV file ', csv_file, 'does not exist')
                    sys.exit(1)
                else:
                    print('CSV file ', csv_file, 'exist')
                    if not csv_file.endswith('.csv'):
                        print(csv_file, 'has no .csv extension')
                        sys.exit(1)
                    else:
                        df = pd.read_csv(os.path.join(args.in_directory, csv_file))
                        # Merge the current DataFrame with the merged_data DataFrame
                        if merged_data is None:
                            merged_data = df
                        else:
                            merged_data = pd.merge(merged_data, df, on=args.key, how=args.join, suffixes=('', f'_{os.path.splitext(csv_file)[0]}'))

            # Sort the merged DataFrame by the 'time' column
            merged_data = merged_data.sort_values(by='time')

            # Save the merged data to a new CSV file
            merged_data.to_csv(os.path.join(args.out_directory, output_name), index=False)                
            print('out-directory has now', os.listdir(args.out_directory), flush=True)

else:
    print('Missing argument --out_directory not exist')
    sys.exit(1)

sys.exit(0)





