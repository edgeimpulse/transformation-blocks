import os, sys, argparse, pathlib

# Set the arguments
parser = argparse.ArgumentParser(description='Organization transformation block')
parser.add_argument('--remote-host', type=str, required=True, help="Remote host to copy files from")
parser.add_argument('--remote-port', type=str, required=True, help="Bucket to store the dataset")
parser.add_argument('--remote-directory', type=str, required=True, help="Remote directory to fetch")
parser.add_argument('--bucket-name', type=str, required=False, help="Bucket to store the dataset")
parser.add_argument('--bucket-prefix', type=str, required=False, help="Output bucket prefix to store the data")

args, unknown = parser.parse_known_args()
remote_host = args.remote_host
remote_port = args.remote_port
remote_directory = args.remote_directory
bucket_name = args.bucket_name
bucket_prefix = args.bucket_prefix
mount_prefix = '/mnt/s3fs/'


# Store files in local /tmp directory if bucket not set (tests only)
if bucket_name is None:
    out_folder = '/home/output/'
else:
    out_folder = os.path.join(mount_prefix, bucket_name, bucket_prefix) if bucket_prefix else os.path.join(mount_prefix, bucket_name)
print('out_folder', out_folder, flush=True)

# Create the output directory if needed
pathlib.Path(out_folder).mkdir(parents=True, exist_ok=True)

# Get ssh credentials
scp_username = os.getenv('SCP_USERNAME')
if not os.getenv('SCP_USERNAME'):
    print('Missing SCP_USERNAME', flush=True)
    sys.exit(1)

scp_password = os.getenv('SCP_PASSWORD')
if not os.getenv('SCP_PASSWORD'):
    print('Missing SCP_PASSWORD', flush=True)
    sys.exit(1)

print("Adding SCP server to known hosts", flush=True)
os.system(f"mkdir -p ~/.ssh && touch known_hosts && ssh-keyscan -p {remote_port} -H {remote_host} >> ~/.ssh/known_hosts")

print("Fetching files from SCP server", flush=True)
os.system(f"sshpass -p {scp_password} scp -r -P {remote_port} {scp_username}@{remote_host}:{remote_directory} {out_folder}")

print("Finished")
sys.exit(0)
