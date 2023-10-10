"""
---
title: Transformers
summary: >
  This is a collection of PyTorch implementations/tutorials of
  transformers and related techniques.
---

# Transformers

This module contains [PyTorch](https://pytorch.org/)
implementations and explanations of original transformer
from paper [Attention Is All You Need](https://papers.labml.ai/paper/1706.03762),
and derivatives and enhancements of it.

* [Multi-head attention](mha.html)
* [Transformer Encoder and Decoder Models](models.html)
* [Position-wise Feed Forward Network (FFN)](feed_forward.html)
* [Fixed positional encoding](positional_encoding.html)

## [Transformer XL](xl/index.html)
This implements Transformer XL model using
[relative multi-head attention](xl/relative_mha.html)

## [Rotary Positional Embeddings](rope/index.html)
This implements Rotary Positional Embeddings (RoPE)

## [Attention with Linear Biases](alibi/index.html)
This implements Attention with Linear Biases (ALiBi).

## [RETRO](retro/index.html)
This implements the Retrieval-Enhanced Transformer (RETRO).

## [Compressive Transformer](compressive/index.html)

This is an implementation of compressive transformer
that extends upon [Transformer XL](xl/index.html) by compressing
the oldest memories to give a longer attention span.

## [GPT Architecture](gpt/index.html)

This is an implementation of GPT-2 architecture.

## [GLU Variants](glu_variants/simple.html)

This is an implementation of the paper
[GLU Variants Improve Transformer](https://papers.labml.ai/paper/2002.05202).

## [kNN-LM](knn/index.html)

This is an implementation of the paper
[Generalization through Memorization: Nearest Neighbor Language Models](https://papers.labml.ai/paper/1911.00172).

## [Feedback Transformer](feedback/index.html)

This is an implementation of the paper
[Accessing Higher-level Representations in Sequential Transformers with Feedback Memory](https://papers.labml.ai/paper/2002.09402).

## [Switch Transformer](switch/index.html)

This is a miniature implementation of the paper
[Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](https://papers.labml.ai/paper/2101.03961).
Our implementation only has a few million parameters and doesn't do model parallel distributed training.
It does single GPU training but we implement the concept of switching as described in the paper.

## [Fast Weights Transformer](fast_weights/index.html)

This is an implementation of the paper
[Linear Transformers Are Secretly Fast Weight Memory Systems in PyTorch](https://papers.labml.ai/paper/2102.11174).

## [FNet: Mixing Tokens with Fourier Transforms](fnet/index.html)

This is an implementation of the paper
[FNet: Mixing Tokens with Fourier Transforms](https://papers.labml.ai/paper/2105.03824).

## [Attention Free Transformer](aft/index.html)

This is an implementation of the paper
[An Attention Free Transformer](https://papers.labml.ai/paper/2105.14103).

## [Masked Language Model](mlm/index.html)

This is an implementation of Masked Language Model used for pre-training in paper
[BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://papers.labml.ai/paper/1810.04805).

## [MLP-Mixer: An all-MLP Architecture for Vision](mlp_mixer/index.html)

This is an implementation of the paper
[MLP-Mixer: An all-MLP Architecture for Vision](https://papers.labml.ai/paper/2105.01601).

## [Pay Attention to MLPs (gMLP)](gmlp/index.html)

This is an implementation of the paper
[Pay Attention to MLPs](https://papers.labml.ai/paper/2105.08050).

## [Vision Transformer (ViT)](vit/index.html)

This is an implementation of the paper
[An Image Is Worth 16x16 Words: Transformers For Image Recognition At Scale](https://papers.labml.ai/paper/2010.11929).

## [Primer EZ](primer_ez/index.html)

This is an implementation of the paper
[Primer: Searching for Efficient Transformers for Language Modeling](https://papers.labml.ai/paper/2109.08668).

## [Hourglass](hour_glass/index.html)

This is an implementation of the paper
[Hierarchical Transformers Are More Efficient Language Models](https://papers.labml.ai/paper/2110.13711)
"""

from .configs import TransformerConfigs
from .models import TransformerLayer, Encoder, Decoder, Generator, EncoderDecoder
from .mha import MultiHeadAttention
from labml_nn.transformers.xl.relative_mha import RelativeMultiHeadAttention
