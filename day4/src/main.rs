use std::fs;

fn problem1(lines: &[&str]) -> i32 {
    let n = lines.len();
    let m = lines[0].len();
    let dirs: &Vec<(i32, i32)> = &vec![(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)];
    let grid = &lines.iter().map(|line| line.chars().collect::<Vec<char>>()).collect::<Vec<Vec<char>>>();
    return grid
        .iter()
        .enumerate()
        .flat_map(|(i, row)| {
            row.iter().enumerate().map(move |(j, char)| {
                if char.eq(&'X') {
                    dirs.iter().filter(|(dr, dc)| {
                        "XMAS".chars().enumerate().all(|(k, c)| {
                            let rr = (i as i32) + dr * (k as i32);
                            let cc = (j as i32) + dc * (k as i32);
                            rr >= 0 && rr < (n as i32) && cc >= 0 && cc < (m as i32) && grid[rr as usize][cc as usize] == c
                        })
                    }).count() as i32
                } else {
                    0
                }
            })
        })
        .sum();

}

fn problem2(lines: &[&str]) -> i32 {
    let n: usize = lines.len();
    let m: usize = lines[0].len();
    let grid: &Vec<Vec<char>> = &lines.iter().map(|line| line.chars().collect::<Vec<char>>()).collect::<Vec<Vec<char>>>();
    return grid 
        .iter()
        .enumerate()
        .flat_map(|(r, row)| {
            row.iter().enumerate().filter(move |(c, char)|{
                if (*char).eq(&'A') && r >= 1 && r < n-1 && *c >= 1 && *c < m-1 {                
                let one: bool = (grid[r-1][c-1] == 'M' && grid[r+1][c+1] == 'S') || (grid[r-1][c-1] == 'S' && grid[r+1][c+1] == 'M');
                let two: bool = (grid[r-1][c+1] == 'M' && grid[r+1][c-1] == 'S') || (grid[r-1][c+1] == 'S' && grid[r+1][c-1] == 'M');
                return one && two;
                } else {
                    return false;
                }
            })
        }).count() as i32;
}

fn main() {
    let contents = fs::read_to_string("day4.txt").unwrap();
    let lines = contents.lines().collect::<Vec<&str>>();
    let res1 = problem1(&lines);
    println!("Result 1: {}", res1);
    let res2 = problem2(&lines);
    println!("Result 2: {}", res2);

}
