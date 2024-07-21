# Modelling Semantic Plausibility

- [Modelling Semantic Plausibility](#modelling-semantic-plausibility)
  - [Introduction](#introduction)
  - [Datasets](#datasets)
  - [Methods](#methods)
  - [Results and Analysis](#results-and-analysis)
      - [Contribution:](#contribution)



## Introduction
**Task:** Semantic PLausibility \
The task involves the evaluation of how plausible or reasonable the sentence is with a given context. This can either be binary classification (plausible, implausible) or multiclasses classification (a scale of plausibility from highly impluasible to highly implausible)


**Research Question:** \
How does the performance change between statistical and neural approaches?

## Datasets
1. [PAP](https://github.com/AnneroseEichel/PAP) (binary and multiclasses)


Each entry consists of a sentence in Subject-Verb-Object (SVO) format along with its corresponding labels for both binary and multiclass settings. In the binary setting, a label of 1 indicates the sentence is plausible, while a label of 0 indicates implausible. In the multiclass setting, the labels range from 1 to 5, with 5 indicating the sentence is highly plausible and 1 indicating it is highly implausible.

**Examples:** \
`1,house curb bike`
`0,pillow scrape plate`

1. [ADEPT](https://aclanthology.org/2021.acl-long.553/) (binary)

Each entry consists of a pair of sentences. The first sentence is the original text, while the second sentence is a modified version with an adjective added to a noun. 

**Examples:** \
sentence 1: `The effect of sleeping is rejuvenation.`
sentence 2: `The effect of additional sleeping is rejuvenation.`

The lebels ranged from 1 to 5, with 5 indicating the sentence is necessarily true and 1 indicating it is impossible.

## Methods

1. [Perceptron](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html)
- Using Word2Vec for CBOW model
- Average word embeddings
- Zero vector for unknown words
- Embedding size = 100
  
1. [RoBERTa](https://huggingface.co/docs/transformers/model_doc/roberta)


## Results and Analysis
See [Semantic_plausibility.pdf](https://github.com/finnique/SemanticPlausibility/blob/main/Semantic_plausibility.pdf)




======================

#### Contribution:
**Nina Vikhrova:**         Data analysis, RoBERTa \
**Mattalika Intarahom:**    Data analysis, Perceptron \
**Martin Wolf:**             Data analysis, Results analysis
