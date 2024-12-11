#!/usr/bin/env python3

from collections import deque

def calculate_trailhead_ratings(map_input):
	# Parse the input map into a 2D grid of integers
	grid = [list(map(int, line)) for line in map_input.strip().split("\n")]
	rows, cols = len(grid), len(grid[0])
	
	def dfs_trail(x, y, current_height):
		"""Recursive DFS to count all distinct paths to height 9."""
		if grid[x][y] == 9:
			return 1  # Reached a valid end point
		
		total_trails = 0
		visited.add((x, y))  # Mark as visited in this path
		for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # All 4 directions
			nx, ny = x + dx, y + dy
			if (
				0 <= nx < rows and 0 <= ny < cols  # Within bounds
				and (nx, ny) not in visited  # Not already visited in this path
				and grid[nx][ny] == current_height + 1  # Valid height increment
			):
				total_trails += dfs_trail(nx, ny, grid[nx][ny])
		visited.remove((x, y))  # Backtrack
		return total_trails
	
	# Find all trailheads and calculate their ratings
	total_rating = 0
	for i in range(rows):
		for j in range(cols):
			if grid[i][j] == 0:  # Trailhead found
				visited = set()  # Reset visited set for each trailhead
				total_rating += dfs_trail(i, j, 0)
			
	return total_rating

def calculate_trailhead_scores(map_input):
	# Parse the input map into a 2D grid of integers
	grid = [list(map(int, line)) for line in map_input.strip().split("\n")]
	rows, cols = len(grid), len(grid[0])
	
	def is_valid_move(x, y, current_height):
		"""Check if a move is valid."""
		return 0 <= x < rows and 0 <= y < cols and grid[x][y] == current_height + 1
	
	def bfs_trailhead(start_x, start_y):
		"""Perform BFS from a trailhead to find all reachable '9' positions."""
		queue = deque([(start_x, start_y)])
		visited = set()
		reachable_nines = set()
		
		while queue:
			x, y = queue.popleft()
			
			if (x, y) in visited:
				continue
			visited.add((x, y))
			
			if grid[x][y] == 9:
				reachable_nines.add((x, y))
				continue
			
			# Check all four directions
			for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
				nx, ny = x + dx, y + dy
				if is_valid_move(nx, ny, grid[x][y]):
					queue.append((nx, ny))
					
		return len(reachable_nines)
	
	# Find all trailheads and calculate their scores
	total_score = 0
	for i in range(rows):
		for j in range(cols):
			if grid[i][j] == 0:  # Trailhead found
				total_score += bfs_trailhead(i, j)
			
	return total_score


# Example topographic map input
map_input = """
967801543219877892110120432456765487321234545
854914678900166743026501501329870398100987656
763023498101255654137432672014981287231892187
012109567692341015048976789023569346542763096
101238747887654320157985989121478965456754345
387345656901298743269834870130327101329805210
296096543214386654978723763243210234910418721
145187762105675667871011054358700195894329652
034219853098734789876012343969656786765012347
124309344565623210985985432878545987787601478
565678234674310301234576501701230834594576569
876569132183087456789632101689321127623987654
985432045092196565410547012678101098210891203
876301896700123478326698763543201543109890312
101216789810156389887789654410892672108701021
560125654327667210796612345329763489807632120
456981011498558976545003459458654308716543031
347876320123443089232117868567761218923784787
210945451056782190101656977657890034874695698
987890102349891001212343980342101125665546788
816543211001230417654322821233211056750036569
105565439814376528740011987344780149821123478
219870126765089439951010476035691231034032107
327892345670129310892312362121003412385221016
456781036789438901765403453438912505496102345
012301095490567812989889854567434676787243212
903432787321054923476798763479823987654356601
876563456434143898565210012189714303498987787
569874894321032387654302100001605212567345698
984965765410101234563218761232556721986432183
673454899006565123870109454343457890673212012
542165678187443012989547823254598012364301501
034078543298332132103456910167652345455677652
125609434701245045892321009878541076210588943
010712549889456756701034569969037889821099812
899823456776321893212103278450126985432178901
701209870125410984345232182321125676589067887
654312565034587654456941091101034389678450996
521023454123898343457850190872765210789321045
438985576540123232567569287963898001679877832
307656987239854101098478016554587123456756921
412587610108763003451289123423696564012345670
653496541067654012760345689510789456703430189
743237832378903009801236776421012329898521278
892106901265012108980109865430101012987630167
"""

# Calculate the sum of trailhead scores
total_score = calculate_trailhead_scores(map_input)
print(total_score)


total_rating = calculate_trailhead_ratings(map_input)
print(total_rating)