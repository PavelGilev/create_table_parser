import internal.preprocessor as ppcss
import internal.scanner as scnnr
import logging

logging.basicConfig(level=logging.INFO, filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

def transform(input: str, output: str):
    file_text = []
    logging.info("Read file %s", input)
    try:
        with open(input ,"r") as f:
            for line in f:
                file_text.append(line)
    except Excetpion as e:
        raise e
    logging.info("Parse file %s", input)
    insructions = ppcss.file_preprocess(file_text)
    logging.info("read file")
    for inrt in insructions:
        if scnnr.is_create_table(inrt):
            logging.info("create table detected: %s", inrt)
