import os

# The input markdown content
input_content = """

---
title: Mitigating Language Confusion through Inference-time Intervention
authors: Yunfan Xie, <strong>Lixin Zou*</strong>, Dan Luo, Min Tang, Chenliang Li, Liming Dong, Xiangyang Luo* (*Corresponding Author)
conference_short: COLING 2025
code:
publication:The 31st International Conference on Computational Linguistics.<strong>(CCF-B)</strong>
pdf: 
code: https://github.com/SoseloX/LSI
---

---
title: META-LORA：Memory-Efficient Sample Reweighting for Fine-Tuning Large Language Models
authors: Weicheng Li, <strong>Lixin Zou*</strong>, Min Tang, Qing Yu, Wanli Li, Chenliang Li (*Corresponding Author)
conference_short: COLING 2025
code:
publication:The 31st International Conference on Computational Linguistics.<strong>(CCF-B)</strong>
pdf: 
code: https://github.com/liweicheng-ai/meta-lora
---

---
title: CHIFRAUD：A Long-term Web Text Benchmark for Chinese Fraud Detection
authors: Min Tang, <strong>Lixin Zou*</strong>, Shiuan-ni Liang, Zhe Jin, Weiqing Wang, Shujie Cui (*Corresponding Author)
conference_short: COLING 2025
code:
publication:The 31st International Conference on Computational Linguistics.<strong>(CCF-B)</strong>
pdf: 
code: https://github.com/xuemingxxx/ChiFraud

---

---
title: Sequential Recommendation by Reprogramming Pretrained Transformer
authors: Min Tang, Shujie Cui, Zhe Jin, Shiuan-ni Liang, Chenliang Li, <strong>Lixin Zou*</strong> (*Corresponding Author)
conference_short: IPM 2025
code:
publication:Information Processing & Management 62 (1), 103938. <strong>(SCI-1, CCF-B)</strong>
pdf: https://www.sciencedirect.com/science/article/pii/S0306457324002978
---

---
title: Spectral and Geometric Spaces Representation Regularization for Multi-Modal Sequential Recommendation
authors: Zihao Li, Xuekong Xu, Zuoli Tang, Lixin Zou, Qian Wang, Chenliang Li (*Corresponding Author)
conference_short: CIKM 2024
code:
publication:The 33rd ACM International Conference on Information and Knowledge Management. <strong>(CCF-B)</strong>
pdf: https://www.sciencedirect.com/science/article/pii/S0306457324002978
---

---
title: TEXT CAN BE FAIR：Mitigating Popularity Bias with PLMs by Learning Relative Preference
authors: Zuoli Tang, Zhaoxin Huan, Zihao Li, Shirui Hu, Xiaolu Zhang, Jun Zhou, <strong>Lixin Zou*</strong>, Chenliang Li* (*Corresponding Author)
conference_short: CIKM 2024
code:
publication:The 33rd ACM International Conference on Information and Knowledge Management. <strong>(CCF-B)</strong>
pdf: https://dl.acm.org/doi/abs/10.1145/3627673.3679581  
---

---
title: Unbiased Recommendation Through Invariant Representation Learning
authors: Min Tang, <strong>Lixin Zou*</strong>, Shujie Cui, Shiuan-ni Liang, Zhe Jin (*Corresponding Author)
conference_short: ECML 2024
code:
publication:Joint European Conference on Machine Learning and Knowledge Discovery in Databases. <strong>(CCF-B)</strong>
pdf: https://link.springer.com/chapter/10.1007/978-3-031-70381-2_18
---

---
title: Efficient Sparse Attention needs Adaptive Token Release
authors: Chaoran Zhang, <strong>Lixin Zou*</strong>, Dan Luo, Xiangyang Luo, Zihao Li, Min Tang, Chenliang Li (*Corresponding Author)
conference_short: ACL Findings 2024
code:
publication:Findings of the Association for Computational Linguistics ACL 2024. <strong>(CCF-A)</strong>
pdf: https://arxiv.org/abs/2407.02328
---

---
title: Unbiased Learning-to-Rank Needs Unconfounded Propensity Estimation
authors: Dan Luo, <strong>Lixin Zou*</strong>, Qingyao Ai, Zhiyu Chen, Chenliang Li, Dawei Yin, Brian D. Davison (*Corresponding Author)
conference_short: SIGIR 2024
code:
publication:The 47th International ACM SIGIR Conference on Research and Development in Information Retrieval. <strong>(CCF-A)</strong> 
pdf: https://dl.acm.org/doi/abs/10.1145/3626772.3657772
# code:
publication:The 47th International ACM SIGIR Conference on Research and Development in Information Retrieval.
---

---
title: Toward Bias-Agnostic Recommender Systems：A Universal Generative Framework
authors: Zhidan Wang, <strong>Lixin Zou*</strong>, Chenliang Li, Shuaiqiang Wang, Xu Chen, Dawei Yin, Weidong Liu (*Corresponding Author)
conference_short: TOIS 2024
code:
publication:ACM Transactions on Information Systems 2024. <strong>(CCF-A)</strong>
pdf: https://dl.acm.org/doi/abs/10.1145/3655617
# code:
publication:ACM Transactions on Information Systems.
---

---
title: Whole Page Unbiased Learning to Rank
authors: Haitao Mao, <strong>Lixin Zou*</strong>, Yujia Zheng, Jiliang Tang, Xiaokai Chu, Jiashu Zhao, Dawei Yin
conference_short: WWW 2024
code:
publication:The ACM on Web Conference 2024. <strong>(CCF-A)</strong>
pdf: https://dl.acm.org/doi/abs/10.1145/3589334.3645474
# code:
publication:The Web Conference.
---

---
title: LT^2R：Learning to Online Learning to Rank for Web Search
authors: Xiaokai Chu, Jiashu Zhao, Changying Hao, Shuaiqiang Wang, Dawei Yin, <strong>Lixin Zou*</strong>, Chenliang Li (*Corresponding Author)
conference_short: ICDE 2024
code:
publication:2024 IEEE 40th International Conference on Data Engineering (ICDE). <strong>(CCF-A)</strong>
pdf: https://ieeexplore.ieee.org/abstract/document/10597769/

---

---
title: Tutorial：Data Denoising Metrics in Recommender Systems
authors: Pengfei Wang, Chenliang Li, <strong>Lixin Zou*</strong>, Zhichao Feng, Kaiyuan Li, Xiaochen Li, Xialong Liu, Shangguang Wang
conference_short: CIKM 2023
code:
publication:The 32nd ACM International Conference on Information and Knowledge Management. 
pdf: https://dl.acm.org/doi/abs/10.1145/3583780.3615297
---

---
title: STRec：Sparse Transformer for Sequential Recommendations
authors: Chengxi Li, Yejing Wang, Qidong Liu, Xiangyu Zhao, Wanyu Wang, Yiqi Wang, <strong>Lixin Zou*</strong>, Wenqi Fan, Qing Li
conference_short: RecSys 2023
code:
publication:The 17th ACM Conference on Recommender Systems. <strong>(CCF-B)</strong>
pdf: https://scholar.archive.org/work/cltegnm76fanjlaowcprddgiri/access/wayback/https://dl.acm.org/doi/pdf/10.1145/3604915.3608779 
---

---
title: Towards Flexible and Adaptive Neural Process for Cold-Start Recommendation
authors: Xixun Lin, Chuan Zhou, Jia Wu, <strong>Lixin Zou*</strong>, Shirui Pan, Yanan Cao, Bin Wang, Shuaiqiang Wang, Dawei Yin
conference_short: TKDE 2023
code:
publication:IEEE Transactions on Knowledge and Data Engineering. <strong>(CCF-A)</strong>
pdf: https://ieeexplore.ieee.org/abstract/document/10227597/
---

---
title: Sample Efficient Offline-to-Online Reinforcement Learning
authors: Siyuan Guo, <strong>Lixin Zou*</strong>, Hechang Chen, Bohao Qu, Haotian Chi, S Yu Philip, Yi Chang
conference_short: TKDE 2023
code:
publication:IEEE Transactions on Knowledge and Data Engineering. <strong>(CCF-A)</strong>
pdf: https://ieeexplore.ieee.org/abstract/document/10227597/ 
---

---
title: Towards Multi-Interest Pre-training with Sparse Capsule Network
authors: Zuoli Tang, Lin Wang, <strong>Lixin Zou*</strong>, Xiaolu Zhang, Jun Zhou, Chenliang Li* (*Corresponding Author)
conference_short: SIGIR 2023
code:
publication:The 46th International ACM SIGIR Conference on Research and Development in Information Retrieval.<strong>(CCF-A)</strong> 
pdf: https://dl.acm.org/doi/10.1145/3539618.3591778
---

---
title: A Survey on Reinforcement Learning for Recommender Systems
authors: Yuanguo Lin, Yong Liu, Fan Lin*, <strong>Lixin Zou*</strong>, Pengcheng Wu, Wenhua Zeng, Huanhuan Chen, Chunyan Miao (*Corresponding Author)
conference_short: TNNLS 2023
code:
publication:IEEE Transactions on Neural Networks and Learning Systems.<strong>(SCI-1, CCF-B)</strong>
pdf: https://ieeexplore.ieee.org/abstract/document/10144689/
---

---
title: Adversarial Multi-Teacher Distillation for Semi-Supervised Relation Extraction
authors: Wanli Li, Tieyun Qian*, Xuhui Li, <strong>Lixin Zou*</strong>
conference_short: TNNLS 2023
code:
publication:IEEE Transactions on Neural Networks and Learning Systems.<strong>(SCI-1, CCF-B)</strong> 
pdf: https://ieeexplore.ieee.org/abstract/document/10083156/ 
---

---
title: User Retention-oriented Recommendation with Decision Transformer
authors: Kesen Zhao, <strong>Lixin Zou*</strong>*, Xiangyu Zhao*, Maolin Wang, Dawei Yin (*Corresponding Author)
conference_short: WWW 2023
code:
publication:Proceedings of the ACM Web Conference 2023. <strong>(CCF-A)</strong>
pdf: https://dl.acm.org/doi/abs/10.1145/3543507.3583418
---

---
title: A Large Scale Search Dataset for Unbiased Learning to Rank
authors: <strong>Lixin Zou*</strong>, Haitao Mao, Xiaokai Chu, Jiliang Tang, Wenwen Ye, Shuaiqiang Wang, Dawei Yin
conference_short: NeurIPS 2022
code:
publication:The 36th Conference on Neural Information Processing Systems. <strong>(CCF-A)</strong>
pdf: https://dl.acm.org/doi/abs/10.1145/3543507.3583418
---

---
title: Pre-trained Language Model based Retrieval and Ranking for Web Search
authors: <strong>Lixin Zou*</strong>, Weixue Lu*, Yiding Liu*, Hengyi Cai*, Xiaokai Chu, Dehong Ma, Dating Shi, Zhicong Cheng, Simiu Gu, Shuaiqiang Wang, Dawei Yin (*Equal Contribution)
conference_short: ACM Transactions on the Web
code:
publication:ACM Transactions on the Web 17 (1), 1-36.<strong>(CCF-B)</strong>
pdf: https://dl.acm.org/doi/abs/10.1145/356868---

---

---
title: Model-based Unbiased Learning to Rank
authors: Dan Luo, <strong>Lixin Zou*</strong>, Qingyao Ai, Zhiyu Chen, Dawei Yin, Brian D Davison
conference_short: WSDM 2023
code:
publication:The 16th ACM International Conference on Web Search and Data Mining. <strong>(CCF-B)</strong>
pdf: https://dl.acm.org/doi/pdf/10.1145/3539597.3570395
---

---
title: Approximated Doubly Robust Search Relevance Estimation
authors: <strong>Lixin Zou*</strong>, Changying Hao, Hengyi Cai, Suqi Cheng, Shuaiqiang Wang, Wenwen Ye, Zhicong Cheng, Simu Gu, Dawei Yin
conference_short: CIKM 2022
code:
publication:The 31st International Conference on Information and Knowledge Management.<strong>(CCF-B)</strong> 
pdf: https://arxiv.org/pdf/2208.07671
---

---
title: A Hierarchical Multi-Granularity Pre-Trained Language Model for Web Search
authors: Xiaokai Chu, Jiashu Zhao, <strong>Lixin Zou*</strong>, Dawei Yin
conference_short: SIGIR 2022
code:
publication:The 45th International ACM SIGIR Conference on Research and Development in Information Retrieval.<strong>(CCF-A)</strong> 
pdf: https://dl.acm.org/doi/pdf/10.1145/3477495.3531986
---

---
title: Contrastive Disentangled Graph Convolutional Network for Weakly-supervised Node Classification
authors: Xiaokai Chu, Jiashu Zhao, Xinxin Fan, Di Yao, Zhihua Zhu, Dawei Yin, <strong>Lixin Zou*</strong>, Jingping Bi
conference_short: DASFAA 2022
code:
publication:The 27th International Conference on Database Systems for Advanced Applications. <strong>(CCF-B)</strong> 
pdf: https://link.springer.com/chapter/10.1007/978-3-031-00123-9_57

---

---
title: Generative Session-based Recommendation
authors: Zhidan Wang, Wenwen Ye, Xu Chen, Wenqiang Zhang, Zhenlei Wang, <strong>Lixin Zou*</strong>, and Weidong Liu
conference_short: WWW 2022
code:
publication:Proceedings of the ACM Web Conference 2022.<strong>(CCF-A)</strong> 
pdf: https://dl.acm.org/doi/pdf/10.1145/3485447.3512095
---

---
title: Fast Semantic Matching via Flexible Contextualized Interaction
authors: Wenwen Ye, Yiding Liu, <strong>Lixin Zou*</strong>, Hengyi Cai, Suqi Cheng, Shuaiqiang Wang, Dawei Yin
conference_short: WSDM 2022
code:
publication:The 15th ACM International Conference on Web Search and Data Mining.<strong>(CCF-B)</strong> 
pdf: https://dl.acm.org/doi/abs/10.1145/3488560.3498442
---

---
title: Pre-trained Language Model based Ranking in Baidu Search
authors: <strong>Lixin Zou*</strong>, Shengqiang Zhang, Hengyi Cai, Dehong Ma, Suqi Cheng, Daiting Shi, Shuaiqiang Wang, Zhichong Cheng, Dawei Yin
conference_short: KDD 2021
code:
publication:The 27th ACM SIGKDD Conference on Knowledge Discovery and Data Mining.<strong>(CCF-A)</strong> 
pdf: https://arxiv.org/pdf/2105.11108  
---

---
title: Enhanced Doubly Robust Learning for Debiasing Post-Click Conversion Rate Estimation
authors: Siyuan Guo, <strong>Lixin Zou*</strong>, Yiding Liu, Wenwen Ye, Suqi Cheng, Shuaiqiang Wang, Hechang Chen, Dawei Yin, Yi Chang (*Corresponding author)
conference_short: SIGIR 2021
code:
publication:The 44th International ACM SIGIR Conference on Research and Development in Information Retrieval.<strong>(CCF-A)</strong> 
pdf: https://arxiv.org/pdf/2105.13623
---

---
title: Data-Efficient Reinforcement Learning for Malaria Control
authors: <strong>Lixin Zou*</strong>, Long Xia, Linfang Hou, Xiangyu Zhao, Dawei Yin
conference_short: IJCAI 2021
code:
publication:The 28th International Joint Conference on Artificial Intelligence.<strong>(CCF-A)</strong> 
pdf: https://arxiv.org/pdf/2105.01620
---

---
title: Whole-Chain Recommendations
authors: Xiangyu Zhao, Long Xia, <strong>Lixin Zou*</strong>, Hui Liu, Dawei Yin, Jiliang Tang
conference_short: CIKM 2020
code:
publication:The 29th International Conference on Information and Knowledge Management.<strong>(CCF-B)</strong> 
pdf: https://arxiv.org/pdf/1902.03987
---

---
title: Deep Multifaceted Transformers for Multi-objective Ranking in Large-Scale E-commerce Recommender Systems
authors: Yulong Gu, Zhuoye Ding, Shuaiqiang Wang, <strong>Lixin Zou*</strong>, Yiding Liu, Dawei Yin
conference_short: CIKM 2020
code:
code:
publication:The 29th International Conference on Information and Knowledge Management.<strong>(CCF-B)</strong> 
---

---
title: Meta-Learning for Neural Relation Classification with Distant Supervision
authors: Zhenzhen Li, Jian-Yun Nie, Benyou Wang, Pan Du, Yuhan Zhang, <strong>Lixin Zou*</strong>, Dongsheng Li
conference_short: CIKM 2020
code:
publication:The 29th International Conference on Information and Knowledge Management.<strong>(CCF-B)</strong> 
pdf: https://www.researchgate.net/profile/Yulong-Gu-5/publication/344752297_Deep_Multifaceted_Transformers_for_Multi-objective_Rank-ing_in_Large-Scale_E-commerce_Recommender_Systems/links/5f8dbf1f299bf1b53e32af1c/Deep-Multifaceted-Transformers-for-Multi-objective-Rank-ing-in-Large-Scale-E-commerce-Recommender-Systems.pdf
---

---
title: Task-based Focal Loss for Adversarially Robust Meta-Learning
authors: Yufang Hou, <strong>Lixin Zou*</strong>, Weidong Liu
conference_short: ICPR 2020
code:
publication:The 25th International Conference on Pattern Recognition.<strong>(CCF-C)</strong> 
pdf: https://ieeexplore.ieee.org/abstract/document/9412701/
---

---
title: Neural Interactive Collaborative Filtering
authors: <strong>Lixin Zou*</strong>, Long Xia, Yulong Gu, Xiangyu Zhao, Weidong Liu, Jimmy Xiangji Huang, Dawei Yin
conference_short: SIGIR 2020
code:
publication:The 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval.<strong>(CCF-A)</strong> 
pdf: https://arxiv.org/pdf/2007.02095
---

---
title: Pseudo Dyna-Q：A reinforcement learning framework for interactive recommendation
authors: <strong>Lixin Zou*</strong>, Long Xia, Pan Du, Zhuo Zhang, Ting Bai, Weidong Liu, Jian-Yun Nie, Dawei Yin
conference_short: WSDM 2020
code:
publication:The 13th ACM International Conference on Web Search and Data Mining.<strong>(CCF-B)</strong> 
pdf: https://tbbaby.github.io/pub/wsdm20.pdf
---

---
title: UserSim：User Simulation via Supervised Generative Adversarial Network
authors: Xiangyu Zhao, Long Xia, <strong>Lixin Zou*</strong>, Dawei Yin, Jiliang Tang
conference_short: WWW 2021
code:
publication:Proceedings of the Web Conference 2021.<strong>(CCF-A)</strong> 
pdf: https://www.cse.msu.edu/~zhaoxi35/paper/www2021usersim.pdf 
---

---
title: Reinforcement learning to optimize long-term user engagement in recommender systems
authors: <strong>Lixin Zou*</strong>, Long Xia, Zhuoye Ding, Jiaxing Song, Weidong Liu, Dawei Yin
conference_short: KDD 2019
code:
publication:The 25th ACM SIGKDD Conference on Knowledge Discovery and Data Mining.<strong>(CCF-A)</strong> 
pdf: https://arxiv.org/pdf/1902.05570
---

---
title: Ctrec：A long-short demands evolution model for continuous-time recommendation
authors: Ting Bai, <strong>Lixin Zou*</strong>, Wayne Xin Zhao, Pan Du, Weidong Liu, Jian-Yun Nie, Ji-Rong Wen (*Co-first author)
conference_short: SIGIR 2019
code:
publication:The 42nd International ACM SIGIR Conference on Research and Development in Information Retrieval.<strong>(CCF-A)</strong> 
pdf: https://www.researchgate.net/profile/Ting-Bai-2/publication/334579722_CTRec_A_Long-Short_Demands_Evolution_Model_for_Continuous-Time_Recommendation/links/5d4160cda6fdcc370a6f3fd1/CTRec-A-Long-Short-Demands-Evolution-Model-for-Continuous-Time-Recommendation.pdf
---

---
title: Reinforcement Learning to Diversify Top-N Recommendation
authors: <strong>Lixin Zou*</strong>, Long Xia, Zhuoye Ding, Dawei Yin, Jiaxing Song, Weidong Liu
conference_short: DASFAA 2019
code:
publication:The 24th International Conference on Database Systems for Advanced Applications.<strong>(CCF-B)</strong> 
pdf: https://link.springer.com/chapter/10.1007/978-3-030-18579-4_7
---

---
title: HLGPS：a home location global positioning system in location-based social networks
authors: Yulong Gu, Jiaxing Song, Weidong Liu, <strong>Lixin Zou*</strong>
conference_short: ICDM 2016
code:
publication:The 16th IEEE International Conference on Data Mining.<strong>(CCF-B)</strong> 
pdf: https://guyulongcs.github.io/files/ICDM2016_HLGPS.pdf:
---


"""

# Split the content into individual entries
entries = input_content.split('---')
entries = [e.strip() for e in entries if e.strip()]

for day, entry in enumerate(entries):
    day = day%20
    day = str(30 - day)
    # Extract title
    title_lines = [line for line in entry.split('\n') if line.startswith('title:')]
    if not title_lines:
        continue
    title = title_lines[0].replace('title: ', '').strip('"').strip()
    
    # Extract date (assuming a default date since none is provided)
    date = "2023-10-01"  # You can modify this or add logic to extract date if available
    
    # Extract authors
    authors_lines = [line for line in entry.split('\n') if line.startswith('authors:')]
    if not authors_lines:
        continue
    authors = authors_lines[0].replace('authors: ', '').strip().strip('"').strip()
    
    # Extract conference_short
    conference_lines = [line for line in entry.split('\n') if line.startswith('conference_short:')]
    if not conference_lines:
        conference_short = ''
    else:
        conference_short = conference_lines[0].replace('conference_short: ', '').strip().strip('"').strip()
    year = conference_short.split(" ")[-1]
    if year == "2025":
        day = str(int(day) - 10)
    # Extract publication
    publication_lines = [line for line in entry.split('\n') if line.startswith('publication:')]
    if not publication_lines:
        publication = ''
    else:
        publication = publication_lines[0].replace('publication: ', '').strip().strip('"').strip()
    publication = publication.strip('publication: ')
    # Extract pdf
    pdf_lines = [line for line in entry.split('\n') if line.startswith('pdf:')]
    if not pdf_lines:
        pdf = ''
    else:
        pdf = pdf_lines[0].replace('pdf: ', '').strip().strip('"').strip()
    pdf = pdf.strip(":")
    # Create filename with sanitized title and date
    # Remove special characters and convert to lowercase
    sanitized_title = title.lower().replace('/', '_').replace('\\', '_').replace(':', '_').replace(' ', '_')
    filename = f"{sanitized_title}_{date}.md"
    
    # Create content for the markdown file
    content = f"""---    
title: "{title}"
collections: publication
permalink: /publication/shadow-removal
excerpt: 'TODO.'
date: {year}-01-{day}
year: {year}
order: 1
is_show: Ture
venue: 
arxiv: 
arxiv_url: 
teaser: 
demo: 
code: 
authors: {authors}
conference_short: {conference_short}
publication: {publication}
pdf: {pdf}
---

"""
    
    # Write to file
    with open(year +"-01-" + day + "-"+ filename, 'w') as f:
        f.write(content)
