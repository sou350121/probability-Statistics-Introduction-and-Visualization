# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 23:26:17 2023

@author: ken3

Introduction:
    LLM
"""

import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

from langchain.agents import Tool
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain import OpenAI
from langchain.agents import initialize_agent

from llama_index import GPTSimpleVectorIndex

index = GPTSimpleVectorIndex.load_from_disk('../vector_indices/index_simple.json')

