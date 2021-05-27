#include <cmath>
#include <stack>
#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>


#define IMPOSSIBLE -1

using namespace std;

class Point {        

  private:
    double x_cord;
    double y_cord;

  public:              

    Point(double x, double y){
        this->x_cord = x;
        this->y_cord = y;
    }

    double get_x() {  
        return x_cord;
    }

    double get_y() {  
        return y_cord;
    }

    static Point middle_with_y(Point first, Point second, double y) {  
        return Point((first.x_cord + second.x_cord) / 2, y);
    }

    double x_distance_to(Point point) {  
        return point.x_cord - this->x_cord;
    }

    double y_distance_to(Point point) {  
        return point.y_cord - this->y_cord;
    }

    double distance(Point point) {
        return sqrt(pow(x_distance_to(point), 2) + pow(y_distance_to(point), 2));
    }

};

// Recursive options
enum EntryPoint {
    CALL,
    RESUME
};


class Context {

  public:              

      int index;
      EntryPoint entry;
      int next_index;
      long long int actual_min;
      long long int min_cost;

    Context(int index, EntryPoint entry) {
        this->index = index;
        this->entry = entry;
        this->next_index = index + 1;
        this->actual_min = IMPOSSIBLE;
        this->min_cost = IMPOSSIBLE;
    }

};

class Land {        


  private:

    int NUM_POINTS;
    int MAX_HEIGHT;
    int ALPHA;
    int BETA;
    stack<Context> my_stack;
    vector<Point> points;

    unsigned long long int pow_long_int(unsigned long long int number) {
        return number * number;
    }

    unsigned long long int cost_arch(Point first, Point second) {
        unsigned long long int distance = first.x_distance_to(second);
        return BETA * pow_long_int(distance);
    }

    unsigned long long int cost_support(Point point) {
        return ALPHA * (MAX_HEIGHT - point.get_y());
    }

    unsigned long long int total_cost(int first_point_index, int second_point_index) {
        return cost_support(points[first_point_index]) + cost_support(points[second_point_index]) + cost_arch(points[first_point_index], points[second_point_index]);
    }

    bool valid_arch(int first_point_index, int second_point_index) {
        Point first_point = points[first_point_index];
        Point second_point = points[second_point_index];
        double radius_value = first_point.x_distance_to(second_point) / 2;
        double init_arch = MAX_HEIGHT - radius_value;
        Point radius_point = Point::middle_with_y(first_point, second_point, init_arch);
        if (init_arch < first_point.get_y() || init_arch < second_point.get_y()) {
            return false;
        } for (int i = first_point_index + 1; i < second_point_index; i++) {
            if ((points[i].get_y() >= init_arch) && pow(radius_point.distance(points[i]), 2) - pow(radius_value, 2) > 0)
                return false;
        }
        return true;
    }

  public:

    Land(int num_points, int height, int alpha, int beta) {
        this->NUM_POINTS = num_points;
        this->MAX_HEIGHT = height;
        this->ALPHA = alpha;
        this->BETA = beta;
    }

    void add_point_to_land(double x, double y) {
        points.push_back(Point(x, y));
    }

    long long int get_minimum_cost() {
        long long int return_ = IMPOSSIBLE;
        my_stack.push(Context(0, CALL));
        while (!my_stack.empty()) {
            Context current = my_stack.top();
            my_stack.pop();
            if (current.entry == CALL) {
                if (current.index + 1 == NUM_POINTS) {
                    return_ = cost_support(points[current.index]);
                } else {
                    current.entry = RESUME;
                    if (valid_arch(current.index, current.next_index)) {
                        current.actual_min = cost_arch(points[current.index], points[current.next_index]) + cost_support(points[current.index]); 
                        my_stack.push(current);
                        my_stack.push(Context(current.next_index, CALL));
                    } else {
                        my_stack.push(current);
                        return_ = IMPOSSIBLE;
                    }
                }
            } else {
                current.next_index += 1;
                if (current.actual_min != IMPOSSIBLE && return_ != IMPOSSIBLE && (current.min_cost == IMPOSSIBLE || (current.actual_min + return_ < current.min_cost))) {
                    current.min_cost = current.actual_min + return_;
                } if (current.next_index == NUM_POINTS) {
                    return_ = current.min_cost;
                } else {
                    current.entry = CALL;
                    my_stack.push(current);
                }
            } 
        }
        return return_;
    }

};

Land get_land_from_file(string file_name) {
    try {
        string line;
        ifstream myfile;
        myfile.open(file_name);
        getline(myfile, line);
        stringstream ss(line);
        string word;
        string constructor[4];
        for (int i = 0; ss >> word; i++)
            constructor[i] = word;
        Land land = Land(stoi(constructor[0]), stoi(constructor[1]), stoi(constructor[2]), stoi(constructor[3]));
        while(getline(myfile, line)) {
            stringstream ss2(line);
            string word2;
            string coord[2];
            for (int i = 0; ss2 >> word2; i++)
                coord[i] = word2;
            land.add_point_to_land(stod(coord[0]), stod(coord[1]));
        }
        myfile.close();
        return land;
    } catch (exception& e) {
        cout << "File " << file_name << " doesn't exist or has invalid syntax \n"; 
        exit(-1);
    }
}

string get_file_name(int argc, char **argv) {
    if (argc == 2)
        return argv[1];
    string file_name;
    cout << "Enter file name: ";
    cin >> file_name;
    return file_name;
}

int main(int argc, char **argv) {
    string file_name = get_file_name(argc, argv);
    Land land = get_land_from_file(file_name);
    long long int minimum = land.get_minimum_cost();
    string result = minimum == IMPOSSIBLE ? "impossible" : to_string(minimum);
    cout << result << "\n" ;
}
