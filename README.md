# Building Autonomous Agents using Autogen

This repository is inspired by Andrew NG's Deeplearning course "AI Agentic Design Patterns with AutoGen" which I highly recommend.

## Autogen Explained - Framework to build Autonomous Agents

Autogen is an open-source multi-agent conversation framework designed to create and manage autonomous agents. It enables these agents to perform tasks, make decisions, and learn independently, reflecting on their actions and improving with minimal human intervention.

## Basic Concepts

Below are some basic building blocks of Autonomous Agents using Autogen.

### Agents

In Autogen, an agent is a unit that interacts with other agents in its environment. Here’s what powers an agent:

1. **LLMs (like GPT-4):** These provide the ability to understand and generate human-like text.
2. **Tool Executors:** These allow the agent to run specific pre-written code.
3. **Code Executors (like an IPython kernel):** These enable the agent to execute code in real-time.
4. **Humans in the Loop:** Humans can step in to guide or correct the agent's actions.

### Fundamental Components of an Autogen Agent

#### Roles and Conversations

In Autogen, you can give roles to agents and have them chat with each other. A conversation is just a series of messages exchanged between agents. These conversations help to move forward on a task.

For instance, in a customer service scenario, you can assign roles to virtual customer service agents and technical support agents to chat with each other, resolving customer issues efficiently through their conversation.

#### Chat Termination

In Autogen, Chat Termination lets you end the conversation between two agents. You can also set a parameter to allow for human intervention. Autogen provides various mechanisms to control AI agent chats, helping to moderate resource consumption and manage costs related to the conversation.

#### Human in the Loop

This feature enables a human to have a conversation with the AI agents by providing feedback on the output to steer the agents in the right direction and specifying goals.

However, you have the option to make the interaction between AI agents completely autonomous by setting the parameter `human_input_mode=NEVER`.

#### Code Executors

Code executors provide agents the ability to execute free-form code if needed during the conversation. They can also augment their free-form code with pre-defined code. Based on the conversation, they can generate code on the fly and then execute it to take actions.

For instance, if an AI agent is asked to generate a stock market chart for Microsoft, it can first plan, then generate necessary free-form code in Python, and then execute the code to create a chart and store it as a `.png` file.

#### Tools Use

Tools in Autogen are pre-defined functions or code that agents can call and use. Instead of writing code from scratch, agents can call tools to perform tasks like searching the web, doing calculations, reading files, or calling remote APIs.

For instance, an agent can use a search tool to find information online or a calculation tool to solve a math problem. By controlling which tools are available to an agent, you control what actions the agent can perform.

### Reasoning and Reflection

Autogen supports various LLM prompting and reasoning strategies, like ReAct and Reflection/Self-Critique. This notebook shows how to implement general LLM reflection with Autogen.

Reflection is a strategy where LLMs analyze outputs and provide feedback.

For example, if you are creating a team for automating the process of blog post writing, you can create an agent that provides critique of the generated writeup, which the writing assistant uses to improve the content.

### Conversation Patterns

Autogen provides several conversation patterns to enable effective and productive communication between a team of agents and humans.

#### Two-agent Chat

It is the simplest form of communication between two agents. For example, simulating a student and teacher interaction when solving a math problem. It has inbuilt functionalities to summarize the conversation too.

#### Sequential Chat

This type of chat is beneficial in task-based scenarios where a complex task can be broken down into interdependent sub-tasks. This is great for scenarios where tasks need to be performed sequentially. For example, in a customer support setting, resolving a technical issue might involve a series of steps: diagnosing the problem, providing troubleshooting instructions, and then confirming the solution with the user. Each step depends on the completion and results of the previous one, making sequential chat an ideal approach to ensure a smooth and efficient resolution process.

#### Group Chat

This type of interaction requires more than two agents and is orchestrated by a Group Chat Manager. The Group Chat Manager selects an agent to speak. The chosen agent sends a message back, which the manager then broadcasts to the other agents. The Group Chat Manager can select the next speaker using various strategies, including round-robin, random, manual, and automatic modes. For instance, this approach can disrupt financial advisory applications by enabling coordinated interactions among multiple AI financial advisors, ensuring structured and comprehensive investment strategies and personalized advice for clients through collaborative decision-making. They are useful for scenarios requiring broad collaboration, such as team discussions, brainstorming sessions, or multi-agent customer service interactions.

#### Constrained Speaker Selection

Group chats can be challenging to manage with many participants. Autogen makes this easier by providing a way to control who speaks next, ensuring smoother transitions between speakers.

#### Nested Chat

Nested chats are used to handle complex tasks by breaking them down into a series of sequential interactions among different agents. In nested chats, an initial message triggers a sequence of subordinate chats, each involving different agents performing specific roles. The nested chat handler coordinates these interactions, ensuring that the output from one agent is passed to the next in the sequence. Ideal for scenarios where a task requires multiple steps or specialized processing, such as writing and reviewing a document, performing a series of calculations, or generating a complex report.

### Cost Optimization

The interactions between agents can become costly since each interaction involves an API call to the LLMs, which charges based on tokens used. Therefore, Autogen provides features to monitor and manage the costs of these interactions effectively.

### Future of Autogen

The future of Autogen is incredibly exciting! This framework is set to continuously evolve, introducing more multimodal features into interactions. Imagine agents not just understanding text, but also seeing and speaking, comprehending visual and audio inputs. This leap will transform interactions, making them more dynamic and immersive than ever before!

