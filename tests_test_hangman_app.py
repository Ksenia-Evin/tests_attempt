import pytest
import sys
from hangman_app import get_word, play, WORDS
import hangman_app


def test_get_word():
    random_word = get_word()
    assert random_word in WORDS

def test_guess_not_a_letter():
    input_value = 1
    word = get_word()
    tries = 4
    hangman_app.input = lambda _: input_value
    with pytest.raises(ValueError):
        play(word, tries)


def test_guess_two_letters_instead_of_one():
    input_value = 'aa'
    word = get_word()
    tries = 4
    hangman_app.input = lambda _: input_value
    with pytest.raises(ValueError):
        play(word, tries)
       

def test_guess_game_over():
    word = get_word()
    tries = 0
    assert play(word, tries) == False
    
@pytest.mark.skip
def test_guess_in_the_word(capsys):
    word = 'skillfactory'
    tries = 4
    guess = word[0]
    hangman_app.input = lambda _: guess
    play(word, tries)
    out = capsys.readouterr()
    assert out == "Good job s is in the word!"
  
@pytest.mark.skip
def test_guess_is_not_in_the_word():
    word = 'lol'
    tries = 4
    hangman_app.input = lambda _: 'g'
    assert play(word, tries) == 'g' + "is not in the word"

