This is a pipeline for processing ebook files. 

Currently, it operates only in the same folder it's deployed in. 

In future, will add ability to take folder argument so that it will start where instructed and also add optional argument for ebook type and expected results. 

Currently takes input file, strips text, returns text and summary analysis information into dataframe in memory. Will also add mandatory to_file argument which will either display, write to file or both, but not hold in memory. 
