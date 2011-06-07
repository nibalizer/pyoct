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
  string xval;
  string yval;
  string zval;
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
  if (myfile.is_open())
  {
    int counter = 0;
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
      thiscarbon.xval=tokens[1];
      thiscarbon.yval=tokens[2];
      thiscarbon.zval=tokens[3];
      thiscarbon.index = counter;
      carbons.push_back(thiscarbon);
     
      hold.push_back(line);
      cout << line << endl;
    }
    myfile.close();
  }

  else cout << "Unable to open file"; 
  count << "derp" << endl;

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

