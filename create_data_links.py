import os
import subprocess

def main():
    input_dir = '/gpfsscratch/rech/wod/umz16dj/Data/MUSTC_v1.0/'
    output_dir = '/gpfsscratch/rech/wod/umz16dj/Data/MUSTC_fairseq/raw'
    splits = ['dev', 'train', 'tst-COMMON', 'tst-HE']
    slangs = ['en']
    tlangs = ['de', 'es', 'fr', 'nl']
    
    for sl in slangs:
        for tl in tlangs:
            for split in splits:
                input_subdir = os.path.join(input_dir, f'{sl}-{tl}/data/{split}')
                output_subdir = os.path.join(output_dir, f'{sl}-{tl}/{split}')
                if not os.path.isdir(output_subdir):
                    os.makedirs(output_subdir)
                h5_input = os.path.join(input_subdir, f'h5/{split}.h5')
                h5_output = os.path.join(output_subdir, f'{split}.h5')
                # h5_output = os.path.join(output_dir, '{}-{}/{}/{}.h5'.format(sl, tl, split, split))
                source_input = os.path.join(input_subdir, f'txt/{split}.{sl}')
                source_output = os.path.join(output_subdir, f'{split}.{sl}')
                target_input = os.path.join(input_subdir, f'txt/{split}.{tl}')
                target_output = os.path.join(output_subdir, f'{split}.{tl}')

                if os.path.isfile(h5_input):
                    # print(f'{h5_input} --> {h5_output}')
                    subprocess.call(["ln", "-s", h5_input, h5_output])
                else:
                    raise Exception(f'File does not exist: {h5_input}')
                
                if os.path.isfile(source_input):
                    # print(f'{source_input} --> {source_output}')
                    subprocess.call(["ln", "-s", source_input, source_output])
                else:
                    raise Exception(f'File does not exist: {source_input}')
                
                if os.path.isfile(target_input):
                    # print(f'{target_input} --> {target_output}')
                    subprocess.call(["ln", "-s", target_input, target_output])
                else:
                    raise Exception(f'File does not exist: {target_input}')

if __name__ == "__main__":
    main()