######################################################################################################
#' You will need to have the data in the format used in the data variable i.e. (utterance_id location_of_file_path)
# If you have the data in the format (/home/shaukat/Linux-work/my-kaldi/kaldi/egs/digits/digits_audio/test/shaukat/1_2_3.wav') then this can be converted into the desired format using the spk2utterance_creation.py file.
# Just uncomment the last lines of the relevant function and the result will be in the console.
######################################################################################################
import inflect

# variable declaration
uttr_ids = []
uttrs_2_speaker = []
words_text = []
wavscp_data = []
nmbr_2_word = {}

# Just paste the audio file paths in the addresses string in the format it is already
addresses = '''/home/shaukat/Linux-work/my-kaldi/kaldi/egs/shaukat-projects/hundred_digits/hundred_digits_audio/train/wajid/0_0_0.wav
/home/shaukat/Linux-work/my-kaldi/kaldi/egs/shaukat-projects/hundred_digits/hundred_digits_audio/train/wajid/0_9_0.wav
/home/shaukat/Linux-work/my-kaldi/kaldi/egs/shaukat-projects/hundred_digits/hundred_digits_audio/train/wajid/1_0_0.wav
/home/shaukat/Linux-work/my-kaldi/kaldi/egs/shaukat-projects/hundred_digits/hundred_digits_audio/train/wajid/1_2_4.wav
/home/shaukat/Linux-work/my-kaldi/kaldi/egs/shaukat-projects/hundred_digits/hundred_digits_audio/train/wajid/1_3_4.wav
/home/shaukat/Linux-work/my-kaldi/kaldi/egs/shaukat-projects/hundred_digits/hundred_digits_audio/train/wajid/1_4_9.wav
/home/shaukat/Linux-work/my-kaldi/kaldi/egs/shaukat-projects/hundred_digits/hundred_digits_audio/train/wajid/1_9_0.wav
/home/shaukat/Linux-work/my-kaldi/kaldi/egs/shaukat-projects/hundred_digits/hundred_digits_audio/train/wajid/2_3_9.wav
/home/shaukat/Linux-work/my-kaldi/kaldi/egs/shaukat-projects/hundred_digits/hundred_digits_audio/train/wajid/2_8_4.wav
/home/shaukat/Linux-work/my-kaldi/kaldi/egs/shaukat-projects/hundred_digits/hundred_digits_audio/train/wajid/3_4_6.wav
/home/shaukat/Linux-work/my-kaldi/kaldi/egs/shaukat-projects/hundred_digits/hundred_digits_audio/train/wajid/3_4_9.wav
/home/shaukat/Linux-work/my-kaldi/kaldi/egs/shaukat-projects/hundred_digits/hundred_digits_audio/train/wajid/3_7_5.wav
/home/shaukat/Linux-work/my-kaldi/kaldi/egs/shaukat-projects/hundred_digits/hundred_digits_audio/train/wajid/3_8_5.wav
/home/shaukat/Linux-work/my-kaldi/kaldi/egs/shaukat-projects/hundred_digits/hundred_digits_audio/train/wajid/4_8_5.wav
/home/shaukat/Linux-work/my-kaldi/kaldi/egs/shaukat-projects/hundred_digits/hundred_digits_audio/train/wajid/4_9_6.wav
/home/shaukat/Linux-work/my-kaldi/kaldi/egs/shaukat-projects/hundred_digits/hundred_digits_audio/train/wajid/5_3_2.wav
/home/shaukat/Linux-work/my-kaldi/kaldi/egs/shaukat-projects/hundred_digits/hundred_digits_audio/train/wajid/5_8_1.wav'''


def wav_scp(addrsz):
  print('\nDATA FOR wav.scp FILE\n')
  addrsz = addrsz.split('\n')
  # print(data)
  for i in range(len(addrsz)):
    pcs_addrsz = addrsz[i].split('/')
    lngth = (len(pcs_addrsz) - 2)
    lst_pcs_data = pcs_addrsz[lngth:]  # pay attention here. put the lenght of the pcs_address list at the place of 13
  # print(lst_pcs_data)
    speaker_name = lst_pcs_data[0]
    utterance_id = lst_pcs_data[0] + '_' + lst_pcs_data[1]  
    utterance_id = utterance_id[0:-4]
    uttr = utterance_id + ' ' + addrsz[i]
    wavscp_data.append(uttr)
    print(uttr)


def uttr_to_number_list(uttr2spkr_data):
  for i in range(len(uttr2spkr_data)):
    nmbr_uttr = uttr2spkr_data[i].split(' ')[0][-5:]
    numbers = list(map(int, nmbr_uttr.split('_')))
    p = inflect.engine()
    words = [p.number_to_words(num) for num in numbers]
    word = ' '.join(words)
    n_nmbr_uttr = 'n'+nmbr_uttr
    nmbr_2_word[n_nmbr_uttr] = word


def utt2spk(data):
  print('\nDATA FOR utt2spk FILE\n')
  for i in range(len(data)):
    uttr_id = data[i].split(' ')[0]

    # appending uttr_ids to the uttr_ids variable for use in other functions
    uttr_ids.append(uttr_id)
    uttr_id = uttr_id + ' ' + uttr_id[0:5]    # adjust it according to the number of letters of the speaker id
    uttrs_2_speaker.append(uttr_id)
    print(uttrs_2_speaker[i])


def text(uttr_id):
  print('\nDATA FOR TEXT FILE\n')
  for i in range(len(uttr_id)):
    uttr = uttr_id[i][-5:]
    n_uttr = f'n{uttr}'
    n_word = nmbr_2_word[n_uttr]
    if(n_word != ''):
      words_text.append(f'{uttr_id[i]} {n_word}')
    print(words_text[i])


def corpus():
  print('\nDATA FOR CORPUS.TXT FILE\n')
  words = list(nmbr_2_word.values())
  for i in range(len(words)):
    print(words[i])


##################################################
          # calling the functions
##################################################
wav_scp(addresses)
utt2spk(wavscp_data)

# helper functions
uttr_to_number_list(uttrs_2_speaker)
text(uttr_ids)
corpus()