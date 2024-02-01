using System;
using System.IO;
using System.Text;


namespace WordCounter
{
    public class TextFile
    {
        private string path;
        private string name;

        public void Files(string path)
        {
            this.path = path;
            this.name = Path.GetFileNameWithoutExtension(path);
        }

        public string[] FileContentToArray()
        {
            char[] separators = {' ', '\n', '\r', '\t'};
            string contentString = File.ReadAllText(this.path, System.Text.Encoding.UTF8);
            string[] words = contentString.Split(separators, StringSplitOptions.RemoveEmptyEntries);

            return words;
        }

        public int CountWordsInArray(string[] words)
        {
            int counter = 0;
            for(int i = 0; i < words.Length; i++)
            {
                if(words[i].ToLower() == this.name.ToLower())
                {
                    counter++;
                }
            }
            return counter;
        }

        public void PrintWordCount(int counter)
        {
            Console.WriteLine($"The word {this.name} appeared {counter} times");
        }

        public string Name { get; set; }
    }
}