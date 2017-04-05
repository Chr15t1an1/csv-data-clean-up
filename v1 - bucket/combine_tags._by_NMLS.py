import csv
import re


#Read file
input_file = open('2015_nmls_contacts_clean_w_tags.csv','r',encoding='utf-8')
csv_obj = csv.reader(input_file)

#Collect data we want
new_list ={}

for row in csv_obj:
    #Fname - Lname - Email
    email = row[0]
    fnam = row[1]
    lnam = row[2]
    nmls =row[3]
    tags =row[4]

    if nmls not in new_list:
        new_list[nmls]={}
        new_list[nmls]['email'] = email
        new_list[nmls]['fname'] = fnam
        new_list[nmls]['lname'] = lnam
        new_list[nmls]['tags'] = tags
        new_list[nmls]['nmls'] = nmls
    else:
        #print('in list')
        new_list[nmls]['tags'] = new_list[nmls]['tags']+tags


input_file.close()

revised_list = []

for var in new_list:
    print(var)
    email = new_list[var]['email']
    fname = new_list[var]['fname']
    lname = new_list[var]['lname']
    tags_c = new_list[var]['tags']
    nmls = new_list[var]['nmls']
    revised_list.append([email,fname,lname,tags_c,nmls])


print(revised_list)




    # new_list.update(
    #     {nmls:
    #          'email': email,
    #          'fnam': fnam,
    #          'lnam': lnam,
    #          'tag': tags,
    #                  })
    # #,fnam,lnam,nmls,tags})


#if email is in list  of emails then add the tag to the existing records

# entries = []
#
# revised_list = []
#
# x = 0
# for i, row in enumerate(new_list):
#     x+=1
#     if x > 1:
#        key = (row[3]) # instead of just the last name
#        if key not in entries:
#            entries.append(key) # Add to list of identified
#            revised_list.append(row)
#            print('not found' + str(i))
#        else:
#             print('key found'+str(i))
#             classTag = row[4]
#             #row[3] = nmls_id in revised_list
#





            # revised_list = []
            #
            # x = 0
            # for i, row in enumerate(new_list):
            #     x += 1
            #     if x > 1:
            #         key = (row[3])  # instead of just the last name
            #         if key not in entries:
            #             entries.append(key)  # Add to list of identified
            #             revised_list.append(row)
            #             print('not found' + str(i))
            #         else:
            #             print('key found' + str(i))
            #             classTag = row[4]
            #             # row[3] = nmls_id in revised_list




                        # Find key in revised list and combine the records
            # for i, row in enumerate(revised_list):
            #     if row[3] == key:
            #         print(i)
            #         tags_c = row[4]
            #         #print(tags_c)
            #         revised_list[i][4] = revised_list[i][4]+tags_c
            #         #revised_list[i][4].join(tags_c)
            #         #print(revised_list[i][4])
#     else:
#         revised_list.append(row)
#
#
#            #.append([row[0],row[1],row[2]])
#
# print(revised_list)


# output_list = []
# i = 0
# for row in new_list:
#     i=i+1
#     id = row[0]
#     if id in output_list:
#         #output_list[output_list.index(id)]
#         print("in list")
#     else:
#         #output_list.append[row]
#         output_list.append([row])
#         print(str(i)+"not in list")
#
# print(output_list)




# #Write to new file
out = open('2015_Tag_Output.csv', 'w', newline='', encoding='utf-8')
output = csv.writer(out)

for row in revised_list:
   output.writerow(row)

out.close()