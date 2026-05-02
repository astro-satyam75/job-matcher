import sqlite3
import pandas as pd

data = [
(1,"Data Analyst","RemoteTech","Remote","Looking for data analyst with Python SQL Excel dashboarding experience"),
(2,"Data Scientist","AI Labs","Remote","Experience in machine learning Python statistics data modeling"),
(3,"ML Engineer","CloudAI","Remote","Build machine learning models using Python TensorFlow deployment"),
(4,"Data Analyst","InsightCorp","Remote","Strong SQL Python Power BI data cleaning visualization"),
(5,"Data Scientist","DeepVision","Remote","Experience with NLP deep learning Python PyTorch"),
(6,"Business Analyst","FinTechX","Remote","SQL Excel stakeholder management dashboards"),
(7,"Data Engineer","DataFlow","Remote","ETL pipelines Python SQL Airflow big data"),
(8,"ML Engineer","VisionAI","Remote","Machine learning models Python scikit learn deployment"),
(9,"Data Analyst","AnalyticsHub","Remote","SQL Excel dashboards business insights"),
(10,"Data Scientist","QuantX","Remote","Statistical analysis machine learning Python R"),
(11,"AI Engineer","NextGenAI","Remote","Machine learning deep learning NLP Python deployment"),
(12,"Data Analyst","MarketPulse","Remote","SQL Excel reporting dashboards analytics"),
(13,"ML Engineer","AutoML Corp","Remote","Model training Python TensorFlow PyTorch cloud"),
(14,"Data Scientist","InsightAI","Remote","Machine learning statistics Python feature engineering"),
(15,"Data Analyst","SalesIntel","Remote","SQL Excel Power BI visualization reporting"),
(16,"Data Engineer","PipelinePro","Remote","ETL pipelines SQL Python Spark Airflow"),
(17,"ML Engineer","AI Systems","Remote","Machine learning algorithms Python scikit learn"),
(18,"Data Scientist","DataMind","Remote","Python machine learning statistics modeling"),
(19,"Data Analyst","BizMetrics","Remote","SQL Excel dashboards insights cleaning"),
(20,"AI Engineer","SmartAI","Remote","Deep learning NLP Python TensorFlow deployment"),
(21,"Data Scientist","CoreAI","Remote","Machine learning Python predictive modeling"),
(22,"Data Analyst","InsightWorks","Remote","SQL Excel Power BI dashboards reporting"),
(23,"ML Engineer","DeepCompute","Remote","Python machine learning TensorFlow deployment"),
(24,"Data Engineer","DataStack","Remote","Python SQL ETL Spark Airflow cloud"),
(25,"Data Scientist","VisionData","Remote","Machine learning Python NLP deep learning"),
(26,"Data Analyst","TrendAnalytics","Remote","SQL Excel dashboards insights visualization"),
(27,"AI Engineer","NeuroAI","Remote","Deep learning NLP Python PyTorch deployment"),
(28,"Data Scientist","QuantifyAI","Remote","Python machine learning predictive modeling"),
(29,"Data Analyst","DataInsights","Remote","SQL Excel Power BI reporting cleaning"),
(30,"ML Engineer","MLWorks","Remote","Machine learning Python scikit learn TensorFlow")
]

df = pd.DataFrame(data, columns=["id","title","company","location","description"])

conn = sqlite3.connect("data/jobs.db")
df.to_sql("jobs", conn, if_exists="replace", index=False)
conn.close()

print("Data loaded successfully")