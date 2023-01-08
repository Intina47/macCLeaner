import os
import  multiprocessing

def delete_duplicates(root_dir):
  file_count = {}
  for root, dirs, files, in os.walk("/"):
    with multiprocessing.Pool() as pool:
      for f in pool.imap_unordered(scan_file,[(root,f) for f in files]):
        if f in file_count:
          file_count[f] += 1
        else:
          file_count[f] =1
        print(f)
  duplicates = [f for f, count in file_count.items() if count > 1]
  if len(duplicates) > 0:
    print("Duplicates:")
    for f in duplicates:
      print(f)
    response = input("Move Duplicates to Bin? (y/n)")
    if response == "y" or "Y":
      for f in duplicates:
        os.remove(f)
      print("Duplicates Successfully Deleted")
    else:
      print("Error: Duplicate not Deleted")
  else:
    print("No Duplicates Found")

def scan_file(args):
  root, f = args
  file_path = os.path.join(root,f)
  return file_path

#run function

if __name__ == '__main__':
  delete_duplicates("/path/to/ios/root/directory")