Data preparation Stage

Read the data and split into train and test TSV in 70:30 ration.
____
data.xml:
    train.tsv
    test.tsv
------

We are chossing only three tags from the data xml. 1. row ID, 2. Title and body 3. Tags (Stack over
tags specific to python)

|Tags|feature name|
|||
|row id| Row ID|
|title and body| text|
|Stackover flow Tags|Label - python|
