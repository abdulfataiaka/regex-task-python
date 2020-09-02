# Import all required modules


class EmailParser:
  pattern = r''  # Provide email pattern here ...
  keys = ['username', 'domain']

  @classmethod
  def parse(cls, url):
    pattern = re.compile(cls.pattern)

    # Add implementation here ...
    pass


#-----------------------------------------------------
# EXPERIMENTS
#-----------------------------------------------------
# Ensure to clear out codes below when you are done
# with experimentations
#-----------------------------------------------------

print('\n>>>> Experiment - EmailParser\n')

result = EmailParser.parse('name@gmail.com')
print(result)
print('')
