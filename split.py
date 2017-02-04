with open('all.txt', 'r') as f:
  with open('jeff.txt', 'w') as jeff:
    with open('casey.txt', 'w') as casey:
      all_lines = f.readlines();
      line_count = len(all_lines)
      for i in xrange(line_count - 1):
        curr_line = all_lines[i].strip()
        if curr_line == "Jeff:":
          jeff.write(all_lines[i + 1])
        elif curr_line == "Casey:":
          casey.write(all_lines[i + 1])
