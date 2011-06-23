// Code © Spencer Krum June 2011
// Released underl GPLv3 See LICENSE file in this repository
// Some of this is takenfrom/inspired by the awesome folks at cpluscplus.com
//
//code to convert xyz files to xyz files with explicit bonds
/*
old format is 
C  xpos ypos zpos 
(tab delimited)

new format

index xpos ypos zpos bondedindex1 index2 index3
(tab delimited)


*/


#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iterator>

using namespace std;

struct carbon
{
  float xval;
  float yval;
  float zval;
  int index;
  int neighbor_1;
  int neighbor_2;
  int neighbor_3;
};


int main () {
  vector <string> hold; 
  vector <carbon> carbons;
  string line;
  ifstream myfile ("xyzfile.txt");
  int counter = 0;
  if (myfile.is_open())
  {
    while ( myfile.good() )
    {
      counter += 1;
      vector<string> tokens;
      getline (myfile,line);
      istringstream iss(line);
      copy(istream_iterator<string>(iss),
              istream_iterator<string>(),
              back_inserter<vector<string> >(tokens));
      for (int i = 0; i < tokens.size(); i++)
      {
          cout << tokens[i] << endl;
      }
      
      carbon thiscarbon;
      cout << tokens[1] << endl;
      cout << atof(tokens[2].c_str()) << endl;
      cout << atof(tokens[3].c_str()) << endl;
      float tok_1 = atof(tokens[1].c_str());
      float tok_2 = atof(tokens[2].c_str());
      float tok_3 = atof(tokens[3].c_str());
      thiscarbon.xval = tok_1;
      thiscarbon.yval = tok_2;
      thiscarbon.zval = tok_3;
      thiscarbon.index = counter;
      carbons.push_back(thiscarbon);
     
      hold.push_back(line);
      cout << line << endl;
    }
    myfile.close();
  }

  else cout << "Unable to open file"; 
  cout << "derp" << endl;

  for (int i = 0; i < hold.size(); i++)
  {
    cout << hold[i] << endl;
  }

  for (int i = 0; i < carbons.size(); i++)
  {
    cout << carbons[i].index << endl;
  }

  return 0;
}

