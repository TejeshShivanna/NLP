Implemented a program that calculates the BLEU evaluation metric, as defined in Papineni, Roukos, Ward and Zhu (2002): Bleu: a Method for Automatic Evaluation of Machine Translation, ACL 2002. The program runs on a set of candidate and reference translations, and calculates the BLEU score for each candidate.

The program will take a two paths as parameters: the first parameter will be the path to the candidate translation (a single file), and the second parameter will be a path to the reference translations (either a single file, or a directory if there are multiple reference translations). The program will write an output file called bleu_out.txt which contains a single floating point number, representing the BLEU score of the candidate translation relative to the set of reference translations.

Notes:
- The candidate and reference files will be in UTF-8 encoding.
- You may assume a line-by-line correspondence of sentences between the candidate and reference translations. 
