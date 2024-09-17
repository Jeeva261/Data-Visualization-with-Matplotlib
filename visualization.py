import pandas as pd 
import matplotlib.pyplot as plt

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\Data-Visualization-with-Matplotlib\file.csv'
df=pd.read_csv(file_path)
print(df)

# plot
plt.plot("ID","Salary",data=df,marker="o")
plt.title("mathplotlib visulization")
plt.xlabel("Age")
plt.ylabel("ID")
plt.show()

# bar plot
plt.bar("City","ID",data=df,color="red",edgecolor="blue")
plt.show()

# hist plot
plt.hist(df["Salary"],color="red",edgecolor="blue")
plt.show()

# scatter plot
plt.scatter("ID","Age",data=df)
plt.grid(axis="x")
plt.show()

# box plot

plt.boxplot(df["Age"],vert=False)
plt.show()

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\Data-Visualization-with-Matplotlib\file1.csv'
df=pd.read_csv(file_path)
print(df)

label=df["City"]
saprated=[0.1,0.2,0.3,0.4,0.5,0.6,0.2,0.6,0.1,0.1]
color=["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#FF8C33", "#33FFF1", "#8C33FF", "#FF3333",
    "#33FF8C"]

plt .pie("ID",data=df,labels=label,explode=saprated,startangle=60,colors=color,)
plt.show()

# heatmap
pv=df.pivot_table(values="ID",index="Age",columns="Salary")
print(pv)

plt.imshow(pv,cmap="viridis")
plt.colorbar()
plt.show()

# subplot
# plot1
plt.subplot(1,2,2)
plt.plot("ID","Salary",data=df,marker="o")
plt.title("mathplotlib visulization")
plt.xlabel("Salary")
plt.ylabel("ID")

# plot 2
plt.subplot(1,2,1)
plt.plot("ID","Age",data=df)
plt.show()


