# git-workshop

Repository for the BIF Software Testing workshop

## Introduction

This is the repository used in the Software Testing Workshop for the WUR Bioinformatics group. This repository contains a number of exercises relating to the workshop, but should stand on their own as well.

This set of exercises only assumes you have python 3.x installed and have a basic familiarity with PIP

1. Clone this repository to begin.
2. Navigate to the repository folder in a shell, then run `python -m unittest`.
    You should see an output like this:

    ```
    $ python -m unittest
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK
    ```

    If you can see the above output, you can continue.
    If the above says something like `Ran 0 tests in 0.000s` let me know (or submit an issue if you are reading this online)

3. Install the coverage module by running `pip install coverage`
4. Start doing exercises!

    - Basic testing exercises are in `exercises/basics.md`
    - Unit testing exercises are in `exercises/unit.md`
    - An exercise for integration testing in `exercises/integration.md`
    - If you have time, extra testing info and exercises are in `exercises/extra.md`

    All commands listed in the exercises are run in the root directory of the repository (the same directory as this readme file).
    It may be a good idea to have an IDE open to modify code while keeping a separate shell to execute commands.


## Reading material

All of the exercises here are using the python built-in unittest, which you can read here: https://docs.python.org/3/library/unittest.html#module-unittest

There is a lot more to testing than is covered in this material.
Of special interest may be the [List of assert methods](https://docs.python.org/3/library/unittest.html#assert-methods)

I did not take any material from the above links, but they may supplement the exercises you find here.

## Note: Usage of AI code generation

GitHub Copilot was used to generate some of the content in this repository, with the exception of this readme file and the markdown files under exercises/

Feel free to use copilot to suggest or generate unit tests for you within this workshop, but note that it is especially important to check tests written by AI, as AI may not understand (or care about, for that matter) the full context of your code and what makes a correct test!

If you are a member of the BIF group, please check if you can use AI code generation in your work outside of this workshop before using it.
