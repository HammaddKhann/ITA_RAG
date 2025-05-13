# ITA_RAG
Built a Game of Thrones chatbot using a RAG pipeline powered by Zephyr-7B and a FAISS-backed document retrieval system. The system is able to answer complex lore-based queries using actual text from the books.

### Dataset Details
We extracted clean, structured text from the official Game Of Thrones series by George R.R. Martin, which includes all seven published books. The dataset had:

      • 70+ chapters parsed and chunked
      
      • Named entities like Jon Snow, Ned Stark, Winterfell preserved
      
      • Dialogue, action, and lore-rich narrative which tested retrieval accuracy

### Architecture Overview
1) Used "all-MiniLM-L6-v2" to embed text chunks and stored them using FAISS for efficient similarity search.
2) Retrieval-Augmented Generation Flow:

          a. Input query is embedded.
         
          b. Top-k similar chunks are retrieved from FAISS.
         
          c. Retrieved context is passed with the query into Zephyr-7B using the HuggingFace pipeline.
   
3) Elected Zephyr-7B-beta for its balanced trade-off between performance and size, integrating it via the HuggingFace transformers pipeline

### Implementation and Experiments
We developed the pipeline in Python via Jupyter Notebook. Highlights:

     • Text chunking and overlap implemented with sliding window logic
     
     • Retrieval system built on FAISS
     
     • Chat interface simulated with input prompts and Zephyr responses
  
Chunk Sizes Tested: 20, 512, 750, 1000, 1500, 50000

Overlap Values: 10, 100, 200, 300, 10000

Generation Parameters:

     • max length = [512, 768, 1024]
     
     • temperature = [0.3, 0.5, 0.7]
     
     • do sample = [True, False]
