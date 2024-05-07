# may-developer-challenge-sap-ai-services
This repository includes examples and additional information for the May Developer Challenge on SAP AI Services - Document Information Extraction and Data Attribute Recommendation.

## Challenge Intro
Welcome to week 1 of the May Developer Challenge on AI at SAP! The topic of this month’s challenge are the AI Services; Document Information Extraction Service and Data Attribute Recommendation. To participate in the challenge you just have to post a screenshot of your solution as a reply in this discussion of the corresponding week.
SAP AI Services help you implement custom use cases by providing powerful algorithms specifically tailored to business problems.

### Document Information Extraction
- The Document Information Extraction service is available in two editions, the original Base Edition and the new genAI-based Premium Edition. The genAI-based Premium edition is using a large language model via generative AI hub on SAP AI Core to extract information from all kinds of documents. 
- With Document Information Extraction you can extract information from the file types PDF or single page JPEG, PNG and TIFF.  
- Supported document types are: invoice, paymentAdvice, purchaseOrder, businessCard, deliveryNote, resume and birthCertificate. 
- You can also extract OCR results directly to process the raw text from you document files as well as use the classification capabilities to classify your documents into the three classes: invoice, purchase order and payment advice.
- You can also enrich your extracted data with your metadata. 
- You can access the Document Information Extraction service via the UI, via swagger/client calls and the Python SDK.

### Data Attribute Recommendation
- With Data Attribute Recommendation you can train your own model to classify data records, predict missing data records
- Data Attribute Recommendation can be used via swagger/client calls as well as the AI API Python SDK
- If you want to access Data Attribute Recommendations via Postman you can download this Postman Collection

# Weekly Challenges
## Week 1 Challenge - DOX UI
This week you will use the UI of the Document Information Extraction service to extract information from your favorite recipe. The UI is great to try out your use case and get a feeling of the capabilities of the service. For productive use cases you would call the APIs or implement a workflow using the Python SDK. Productively, you could then for example implement a workflow that processes documents right out of your mailbox, saves the extracted information in the system and structure you need as well as triggers other necessary workflows.
For this week’s challenge, use the UI to extract the header fields “recipe name”, “portions” and the line items “quantity” and “ingredient” from your chosen recipe. Therefore, you need to create a custom schema. Make sure the recipe is in one of the supported languages.
When creating a custom Schema chose the Setup Type auto to use the llm/genAI-based Premium Edition. In the description field provide information for the large language model to understand what you are referring to e.g. “the name of the recipe”.

<img width="468" alt="image" src="https://github.com/noravth/may-developer-challenge-sap-ai-services/assets/29603544/bdb24896-cdcc-4749-91ce-4714d43b6017">

1. Get a free trial account and run DOX booster: https://developers.sap.com/tutorials/cp-aibus-dox-booster-key.html 
2.	Get the Document Information Extraction UI: https://developers.sap.com/tutorials/cp-aibus-dox-ui-sub.html
3.	Create a custom schema: https://developers.sap.com/tutorials/cp-aibus-dox-ui-gen-ai.html
4.	OPTIONAL: Create a template and add your document to the template (improves performance for future recipes)
5.	Upload your favorite recipe to extract the name, portions, quantity and ingredients. Make sure your recipe pdf is only 1 or 2 pages long, otherwise you will quickly reach the limit (50 pages) of the trial plan.
6.	Submission: share a screenshot of the extraction results and the document and write a comment to share your experience using the UI in the discussion below.

Example Screenshot:

<img width="468" alt="image" src="https://github.com/noravth/may-developer-challenge-sap-ai-services/assets/29603544/72fd0752-730f-47e5-afb7-891c3e400a6a">

### Additional Information
- [Processing a ©Pokémon Card in 90 seconds with Document Information Extraction powered by generative AI](https://community.sap.com/t5/technology-blogs-by-sap/processing-a-pok%C3%A9mon-card-in-90-seconds-with-document-information/ba-p/13571759)
- Be aware of [limits that apply in free tier and trial accounts](https://help.sap.com/docs/document-information-extraction/document-information-extraction/free-tier-option-and-trial-account-technical-constraints)
- How to [improve your results](https://help.sap.com/docs/document-information-extraction/document-information-extraction/best-practices-298a9a0936d5436494c644ec51bbdcea)
- If you do not want to run the booster for Document Information Extraction make sure to register to the service using the blocks_of_100 service plan and assign the necessary role collections to your user.
- In [this “2-min of” video](https://youtu.be/w66uwSWGvH0) I am describing the technical aspects of the BASE service (without use of LLM) behind the scenes. 

## Week 2 Challenge - DOX Python SDK
Thank you so much for your participation last week and the great results! I am so happy to see your drive and experimental mindsets! I also really love the inspiration I got from all your favorite recipes! I will definitely try them out! And I loved the M-AI Developer Challenge pun comment!

This week we want to use the [Document Information Extraction Python SDK](https://pypi.org/project/sap-business-document-processing/) to extract information from the same recipe from week 1 using the custom schema you in the Document Information Extraction UI. With the Python SDK you can implement end-to-end use cases and process documents on a large scale.

1.	Use the Python IDE of your choice, create and activate a virtual environment and install the [Document Information Extraction Python SDK](https://pypi.org/project/sap-business-document-processing/) 
2.	Optional: Only needed if you want to use utils to display capabilities and display extraction: Install other dependencies (PyPDF2, fpdf, IPython)
3.	Get your Document Information Extraction service key from your BTP trial account
4.	Send your document from week 1 to the Document Information Extraction instance via the Python code (you can use the default client)
5.	You will need your Schema ID which you can fine in the URL of the UI when navigated to the schema you want to use.
   
<img width="468" alt="image" src="https://github.com/noravth/may-developer-challenge-sap-ai-services/assets/29603544/12480225-6400-4925-8f3f-c08e655d90ec">

7.	[Example code](https://github.com/noravth/may-developer-challenge-sap-ai-services/blob/main/document_information_extraction.py)
8.	Additional information: Check out [this](https://github.com/SAP/business-document-processing/blob/main/examples/document_information_extraction_examples/information_extraction_showcase.ipynb) example code with more examples

To SUBMIT your result simply reply to this discussion by pasting an image with your code and returned json like this: 

<img width="468" alt="image" src="https://github.com/noravth/may-developer-challenge-sap-ai-services/assets/29603544/0eaa77b5-4d1f-484d-8d36-a72ff757ad1c">


