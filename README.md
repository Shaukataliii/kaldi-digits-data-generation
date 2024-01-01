This code creates wav.scp, utt2spk, text and corpus files of audios (as used in the kaldi for dummies tutorial)

We assume that you’ve python3 and the python inflect library set up in your system. So just open the file in code editor and you are good to go.

How to use?

You have to copy the audios and paste them into a text editor. In this way you will get the paths of all the audios (one on each line)

Now copy those paths and paste them in the {addresses} variable. Now just run the file. You will get the data of the wav.scp, utt2spk, text and corpus files.

You can modify the line no. 70 where it says:

uttr_id = uttr_id + ' ' + uttr_id[0:5]    # adjust it according to the number of letters of the speaker id

Now, it should work fine.
