from pathlib import Path

def prepare_test(case_path: Path, sol_path: Path, save_dir: Path):

    input_txt = [filee for filee in case_path.glob('*.txt')]
    output_txt = [filee for filee in sol_path.glob('*.txt')]
    assert len(input_txt) == len(output_txt), "Inputs and outputs are not compatible"

    for idx, filename in enumerate(input_txt):
        file_number = str(filename).split('.')[0].split('/')[-1]
        file_number = int(file_number)
        inplist = outlist = None


        with open(filename, mode = 'r', encoding='utf-8') as reader:
            inplist = reader.readlines()
        reader.close()

        with open(output_txt[idx], mode = 'r', encoding= 'utf-8') as reader:
            outlist = reader.readlines()
        reader.close()
        # breakpoint()
        inp = out = "" 
        for item in inplist:
            inp += str(item)
        for item in outlist:
            out += str(item)
        with open(save_dir / f'{file_number}.txt', mode = 'w', encoding='utf-8') as writer:
            body = f'input = """{str(inp)}"""\n\nexpect = "{str(out)}"'
            writer.write(body)
        writer.close() 

if __name__ == '__main__':

    BASEDIR = Path('/home/quangng/Desktop/Github/PPL/assignment3/src/test')
    SOL = BASEDIR / 'solutions'
    CASE = BASEDIR / 'testcases'
    SAVE = BASEDIR / 'save'
    # SAVE.mkdir(parents = True, exist_ok=True)

    prepare_test(CASE, SOL, SAVE)