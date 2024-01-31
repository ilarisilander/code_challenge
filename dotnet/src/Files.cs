using System;
using System.IO;
using System.Text;


namespace WordCounter
{
    public class Files
    {
        private string path;
        private string name;

        public Files(string path)
        {
            this.path = path;
            this.name = Path.GetFileNameWithoutExtension(path)
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

        public string GetName()
        {
            return this.name;
        }

        public void SetName(string name)
        {
            this.name = name;
        }
    }
}