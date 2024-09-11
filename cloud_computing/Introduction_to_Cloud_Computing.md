Why do we need to think about infrastructure scalability?



                         Applications are generally grouped into two broad classes
1.  Latency-sensitive or user facing jobs
2.  Throughput oriented or batch processing jobs

In healthcare, we now have the capability to collect petabytes of health data for just one individual. At Stanford University, we collected over 2 PB of data around Dr. Michael Snyder, Chair and Professor of Genetics at Stanford University. 
However, only storing a petabyte of data on any major cloud provider can cost up to $20,000 per month. Clearly, we need better computational and storage systems.

                       Capacity planning: Ensure resources are available to your growing workload.
Capacity planning is the process of determining the production capacity, and making sure your business has the available resources to meet consumer demand.

In 2008, Amazon found that every 100ms of latency cost them 1% in sales. In 2006, Google found an extra 0.5 seconds in search page generation time dropped traffic by 20%. 
According to Google Analytics data, 53% of visits are abandoned if a mobile site takes longer than 3 seconds to load. [6]

Response time is critical for healthcare applications, such as detecting heart failure, seizure, and epilepsy in children. The question to ask is: How can we make sure we have enough servers to process a large number of requests at any moment?

                    Pay-as-you-go: Pay as much as you use the cloud resources.
For most services we use in the market, we are responsible for paying for the services. It is no exception if we use cloud computing services. Pay-as-you-go model describes that customers pay for the cloud services based on their usage, rather than a flat rate.
Keep in mind, this model is what we use in cloud computing. The service being charged is the computer utilities. We will explain more next.

                    Utility computing: Manage your cloud usage.
Utility computing allows customers that use cloud services to manage their computer utilities usages. This is important because it provides customers the flexibility to choose which services they will use based on their changing needs. 
In addition, it saves customers lots of money because the pay-as-you-go model is now possible with utility computing.

n the setting of cloud computing, utility computing is what makes pay-as-you-go model possible for the customers. Essentially, utility computing is a service provisioning model set by cloud service providers.
It allows customers to use the service in a more cost-efficient way.

P.S. Leonard Kleinrock is one of the key scientists behind creating The Advanced Research Projects Agency Network (ARPANET) project – the first public packet-switched computer network – which led to the creation of the Internet.

                   What is elasticity?
Elasticity is defined as the ability to scale computing resources dynamically based on the size of workload. A cloud customer can add or remove computing, storage, and networking assets based on their needs. 
For example, Amazon Elastic Compute Cloud (Amazon EC2) provides its customers resizable compute capacity to support their dynamic workloads.

                 What is Cloud Computing?
Cloud computing is services, such as servers, storage, databases, and networks on the Internet (also called cloud, or a network of servers) that the customers can use based on their unique needs at the time, and only pay for their usage. [8]

According to the National Institute of Standards and Technology (NIST) [1]:

“Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) 
that can be rapidly provisioned and released with minimal management effort or service provider interaction.”

                 Virtualization: The piece that makes cloud computing possible
Virtualization is the making of a virtual computer that performs the same function as a physical computer. While having the same functionalities of a physical computer, it is more flexible and powerful than a physical computer.

Imagine having several servers, operating systems, and applications running on one physical computer. This is what cloud computing allows us to do [12]. For example, if you are running a pharmaceutical startup, 
your employees can use your company’s physical computer hardware more efficiently with cloud computing. They can run more data and algorithms with just one computer, and generate more results for your company in a single day. 
Essentially, they can do more “jobs”. Cloud computing is a great return on investment for a business, and provides your company with a competitive edge.

The physical computer we interact with is used like a building. Without cloud computing, there is only one room inside with one living room, kitchen, bathroom, and balcony (eg. one server, one operating system).
With cloud computing, there are several rooms in different shapes and sizes. What’s great is that the guests that will move into these rooms decide the shape and sizes of these rooms. 
In the context of cloud computing, we decide what we will include in our room (i.e. our virtual machine) depending on the job we will perform: do we need storage? Do we need computers?

The additional benefit of cloud computing using the metaphor of the building is that if the kitchen in one room is broken, it won’t affect the kitchen in other rooms. Therefore, other jobs won’t be affected if one job is paused.

               What are the service models for cloud computing?
Traditionally, teams were in charge of the full technology stack from buying servers and storage, to configuring computer networks and installing operating systems (OS) – this was called on-premises. 
Data center is an organization’s physical facility that hosts data and applications with the organization’s computing resources, storage, and network infrastructures. 
This model is like having your own dedicated kitchen, and buying all the ingredients to cook a pizza.

With the emergence of Cloud Computing, infrastructure moves from physical servers to virtual networks. This allows us to use multiple servers from different data centers at once. 
In other words, when we are hosting data or applications in the cloud, we are using resources from different data centers managed by the cloud provider [11].
Now we know that the services cloud providers offer are essentially on-demand data center resources. 

              Based on our needs, there are 3 types of service models
1) Infrastructure-as-a-Service (IaaS)
This model is like you bring pizza ingredients to a shared oven at a community kitchen, where they have set up the infrastructure for you to cook. You have complete control over the cooking process.

In the IaaS model, cloud providers are responsible for physical infrastructure, such as buying servers, storage, and handling virtualization. Amazon Elastic Compute Cloud (Amazon EC2) is an example of IaaS. 
You have complete control over the configuration of your cloud resources.

Note the networking layer is a shared responsibility between the provider and customer.

2) Platform-as-a-Service (PaaS)
If you order a pizza delivery from a restaurant, the only thing that you need to think about is how you want to create the pizza, such as what toppings you want to have, and a thicker Sicilian pizza or a thin New York pizza.
You leave the rest of the tasks to the restaurant, such as setting up the kitchen, and sourcing ingredients.
In the context of cloud computing, PaaS allows customers to focus on developing applications and algorithms, by providing infrastructure, and support on building, testing, deploying, managing, and updating.
For example, Amazon SageMaker allows bioinformaticians to build, train, and deploy machine learning models. Amazon Athena and Google BigQuery are another two examples of this service model.

Cloud providers are handling the technology stack up to the middleware layer – Middleware is software that performs like a bridge between different applications. 
For example, messaging systems like Amazon Simple Notification Service (NAS) or Google PubSub are considered middleware.

3) Software as a Service (SaaS)
As the name suggests, SaaS companies rent the software services to its customers via the Internet [9]. The experience of using SaaS is like dining in at a nice restaurant to celebrate you graduating college.
As a customer, you pay for an out of package solution for the experience of having food served to you in a thoughtfully decorated environment. You’re only responsible for showing up, and deciding who you are going to invite to share the dinner.
The restaurant will take care of the rest.

For the SaaS model, cloud providers are in charge of most of the technology stack – the only shared layer is around data. Examples of SaaS are Google Doc, Zoom, and Amazon Simple Storage Service (Amazon S3). 
Even though cloud providers host customer's datasets, customers are responsible for specifying who can have access to the datasets.

                   What are the deployment models?
Deployment models determine the specific types of cloud environment based on ownership and access, as well as the cloud's scope and purpose [2].
National Institute of Standards and Technology (NIST) defines four cloud deployment models:

1. Public
2. Private
3. Community
4. Hybrid

Let’s assume we want to deliver some boxes from point A to Z and we have two options: 1) regular truck or 2) armor truck. Which one would you pick?

The cost of using an armored car is more than a regular car, but the important question to ask is: what are we trying to deliver? If we plan to deliver gold, then it makes sense to go with an armor truck. 
However, if we are delivering something less valuable like copper, then a typical truck is likely to be good enough.

1. Private cloud:

We can consider a private cloud like an armor truck that is dedicated to our needs, and each data center where the resource belongs to is exclusive to one organization. If one machine is down, then we won’t need to worry about the rest of the machine.

2. Public cloud:

In comparison, public cloud is a shared infrastructure like UPS (United Parcel Service), where our boxes are on a shared facility.

3. Community cloud:
Community cloud is an exclusive use by a specific community of consumers from organizations that have shared concerns (e.g. mission, security requirements, policy, and compliance considerations).
For example, AWS GovCloud (US) is an example of a community cloud. It helps its customers support US government compliance requirements. [7]

5. Hybrid cloud: As the name suggests, it is a composition of two or more distinct cloud infrastructures (private, community, or public). For example, we could deliver copper with a public truck to a middle point, and then deliver gold from the middle point to the Z point using an armor truck.


Question 1

The cloud infrastructure is provisioned for exclusive use by a single organization comprising multiple consumers (e.g., business units).

i. Private  ====> COREECT ANSWER

ii. Public

iii. Community

iv. Hybrid

Question 2

What is elasticity?

i. A cost model for cloud services that encompasses both subscription-based and consumption-based models

ii. Ability to increase performance by adding more resources for a fixed workload size

iii. Ability to scale resources dynamically based on the size of workload ====> COREECT ANSWER

iv. A percentage of the time a system is expected to be available, e.g., 99.999 percent ("five nines")

Question 3

The cloud infrastructure is provisioned for exclusive use by a specific community of consumers from organizations that have shared concerns (e.g., mission, security requirements, policy, and compliance considerations).

i. Private

ii. Public

iii. Community  ====> COREECT ANSWER

iv. Hybrid

Question 4

What are the main service models according to NIST?

i. IaaS, PaaS, SaaS ====> COREECT ANSWER

ii. Public/Private/Community Cloud

iii. IaaS, Public Cloud

iv. on-premise, IaaS, PaaS, FaaS

Question 5

The cloud infrastructure is provisioned for open use by the general public.

i. Private

ii. Public  ====> COREECT ANSWER

iii. Community

iv Hybrid
