Q1-Extract all karakas and their respective vibhaktis along with sentences from a Hindi treebank.
==============================================================================================

As per my understanding SSF Tree banks having four column seprated by "tab" Namely:
1-Address, 2-Token, 3-Category, 4-Attribute-value pairs
 
4-Attribute-value pairs:
This column contained the the Feature Structure tag <fs> -
<fs> tag having abbreviated attributes or called 'af'.
The field for each attribute is at a fixed position, and a comma is used as a separater.
Thus, in case, no value is given for a particular attribute the field is left blank.
Fixed position of each attribute-
        1-> Root
        2-> Cat
        3-> Gender
        4-> Number
        5-> Person
        6-> Case
        7-> Case Marker/Vibhakti
        8-> Suffix 

Interlinking of nodes:
Nodes might be interlinked with each other through directed edges. Usually, these edges have nothing to do with phrase structure tree, and are concerned with dependency structure, thematic structure, etc. These are specified using the attribute value syntax, how ever, they do not specify a property for a node, rather a relation between two nodes.

```
	- So as per question requirment we have to do following task--
    	- Extract the 'KARAKAS' from the <fs> tag using keyword "drel", drel represent dependency relation between nodes.
	- Extract 'VIBHAKTI' from the af. In af 'Case Marker/Vibhakti' on 7th postion. 
```

#	Following Assumption I have made:
	######	Output Format:
        ```
		Hindi Sentence:
		गढ़ मुक्तेश्वर का वर्णन शिव पुराण में मिलता है ।

            	Karakas/Dependency relation in Sentence are :
            	drel='r6:NP2' drel='k1:VGF' drel='k7:VGF' drel='rsym:VGF'

            	Vibhakti/Case Marker in Sentence word by word () are :
		गढ़(0) मुक्तेश्वर(0) का() वर्णन(0) शिव(0) पुराण(0) में() मिल(ता) है(है)
	```	
		--	Where Vibhakti display in following format: 
				Word(Vibhakti)===> मिल(ता) 
				
	######	Follow the following steps to execute the programs:
		Extaract the Directory with name 'NLP-Internship-V0.1'
		$ cd NLP-Internship-V0.1
		$ python3 sentence-separator.py -i=ssf_file_name
			Sentence seprated files are created and saved in the directory "input_dir"
        	$ sh run.sh input_dir/ output_dir/
            		Output file created and save in the directory "NLP-Internship-V0.1" with the name of "out.ssf"
            
	## For example
		$ cd NLP-Internship-V0.1
		$ python3 sentence-separator.py -i=Data/mor-1-50-posn-name.txt
        	$ sh run.sh input_dir/ output_dir/


Version-0.1
Auther- Vilal Ali
Thanks for using program, Enjoy!
