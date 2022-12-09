# Parse the input and build the filesystem
filesystem = {'type': 'dir'}
cur_dir = '/'

with open('input.txt') as f:
    input_lines = f.readlines()


def modifyFs(cur_dir, directory):
    if cur_dir == '/' or cur_dir == '':
        return directory
    path = cur_dir.split('/')
    for i in range(len(path)):
        p = path[i]
        if p == '': 
            continue
        return modifyFs('/'.join(path[i+1:]), directory[p])
    

for line in input_lines:
    line = line.strip()
    if line[0] == '$':
        # Parse the command
        cmd, *args = line[1:].split()
        if cmd == 'cd':
            # Change directory
            if args[0] == '/':
                # Go to the root directory
                cur_dir = '/'
            elif args[0] == '..':
                # Go to the parent directory
                cur_dir = ''.join(cur_dir.rpartition('/')[:-1])
                if cur_dir[-1] == '/':
                    cur_dir = cur_dir[:-1]
            else:
                # Go to a child directory
                if cur_dir == '/':
                    cur_dir = cur_dir + args[0]
                else:
                    cur_dir = cur_dir + '/' + args[0]
        elif cmd == 'ls':
            pass
    else:
        # Parse and add the file or directory to the current directory
        parts = line.split()
        if parts[0] == "dir":
            dir_name = parts[1]
            directory = modifyFs(cur_dir, filesystem)
            directory.update({dir_name: {'type': 'dir'}})
        else:
            file_name = parts[1]
            file_size = int(parts[0])
            directory = modifyFs(cur_dir, filesystem)
            directory.update({file_name: {'type': 'file', 'size': file_size}})


# Traverse the filesystem and calculate the total size of each directory
dir_sizes = {}


def dfs(dir_name, directory):
    # Calculate the total size of this directory
    total_size = 0

    # print(directory)
    if directory['type'] == 'file':
        return directory['size']

    for name in directory:
        if name == 'type':
            continue
        if dir_name == '/':
            new_dir_name = dir_name + name
        else: 
            new_dir_name = dir_name + '/' + name
        total_size += dfs(new_dir_name, directory[name])

    dir_sizes[dir_name] = total_size

    return total_size

dfs('/', filesystem)

# Find the directories with a total size of at most 100000
total_size = 0
for dir, size in dir_sizes.items():
    if size <= 100000:
        total_size += size

print(total_size)
