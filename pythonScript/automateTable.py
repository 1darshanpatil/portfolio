#-----------------------------------------------------------------------------------------------------------------------------------------------------#
# The purpose of this Python script is to read the contents of an HTML file containing a list of repositories,                                        #
# extract relevant information such as the repository name, description, and last updated date using the BeautifulSoup library,                       #
# and then write this information into a new HTML file in the form of a table. The resulting table includes columns for the repository name,          #
# description, and last updated date, and each row represents a single repository from the original list.                                             #
#-----------------------------------------------------------------------------------------------------------------------------------------------------#




from bs4 import BeautifulSoup

with open('file1.html', 'r') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

repo_list = soup.find('ul')

with open('table.html', 'w') as f:
    f.write('<table>\n')
    f.write('  <thead>\n')
    f.write('    <tr>\n')
    f.write('      <th>Repository</th>\n')
    f.write('      <th>Description</th>\n')
    f.write('      <th>Last Updated</th>\n')
    f.write('    </tr>\n')
    f.write('  </thead>\n')
    
    f.write('  <tbody>\n')
    for repo in repo_list.find_all('li'):
        repo_name = repo.find('a').text
        repo_url = repo.find('a')['href']
        
        repo_desc = repo.text.split(' - ')[1]
        
        try:
            repo_date = repo.text.split('(')[-1].strip(')\n')
        except IndexError:
            repo_date = ''
        
        f.write('    <tr>\n')
        f.write(f'      <td><a href="{repo_url}">{repo_name}</a></td>\n')
        f.write(f'      <td>{repo_desc}</td>\n')
        f.write(f'      <td>{repo_date}</td>\n')
        f.write('    </tr>\n')
    f.write('  </tbody>\n')
    f.write('</table>\n')
