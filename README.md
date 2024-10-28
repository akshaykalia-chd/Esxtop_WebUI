# Fork of esxtop drill V2

The project is attempt to make the application 
- System UI compatible using MAC
- System UI compatible with Ubuntu
- Convert to an API driven webapp

### Starting the Mac app
1. Download the Mac_Application Dir
2. Navigate to Mac_Application/EsxtopDrill/
3. Double Click EsxtopDrill
4. Wait for application to load 
5. For the first Run application can take some time at the bellow screen ![img.png](img.png)
6. Once the application has started you should see below UI ![img_1.png](img_1.png)
7. The application log can be found under ~/esxtop_drill.log


### Using the app

1. Select the Working Directory. This is the location where all the output files will be stored. Each counter group will have its on Directory.
2. Load The CSV 
3. Provide the Name of the Object. This can be a VM, Naa ID, NIC etc. You can leave it blank as well. In this case the output will not be filtered for the object 
3. Drop System Objects if you are working with an Object level issue, else you can ignore this step
4. Use Fault Finder or Drops downs to check on various counters in the data
