select m."venue" , m."season" , d."bowler", 
d."batting_team" as against_team,
count(extra_runs) as extras
from deliveries as d
left join matches as m on m."match_id" = d."match_id"
where d."extra_runs" > 0
group by m."season" , m."venue" , d."bowler" , d."batting_team" 
order by m."season" , m."venue" , d."bowler" , d."batting_team";