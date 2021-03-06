![example.png](https://raw.githubusercontent.com/jedevc/rngback/master/example.png)

# rngback

rngback is a simple, easy-to-use tool to randomly generate visually pleasing
backgrounds.

## Installation

To setup rngback, clone the repo and then run `setup.py`.

	$ git clone https://github.com/jedevc/rngback.git
	$ cd rngback
	$ python setup.py install

You should then be able to access the `rngback` command. If not, then make
sure that the pip installation directory is added to your `PATH`.

## Example usage

Generate a 400x600 image, with 20x30 squares.

	$ rngback 400 600 10 15

Generate the same thing but with an blue foreground and a darkblue background.

	$ rngback 400 600 10 15 -fg blue -bg darkblue

Add some variation to the foreground.

	$ rngback 400 600 10 15 -fg blue -bg darkblue -var 40

Randomize the foreground to a different shade of blue each time and a black
background.

	$ rngback 400 600 10 15 -fg 'hsl({160-240}, {50-70}%, 60%)' -bg darkblue -var 40

Create gaps between the squares.

	$ rngback 400 600 10 15 -fg blue -bg darkblue -off 2

## More

rngback comes with a builtin help. To view it, simply run:

	$ rngback --help
