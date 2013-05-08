require 'rake/distribute'
require 'rake/clean'
require 'facets/string'
project_name = __FILE__.pathmap("%-1d")

def version
  project_readme = FileList['README.*']
  version_re = /Version \s+ : \s* (?<version> \d\.\d\.\d) $/x

  project_readme.each { |f| 
    File.read(f).mscan(version_re).each { |m| 
      return m[:version]
    }
  }
end

powerline_src = File.expand_path('~/.vim/bundle/powerline')

desc "diff from system default config"
task :diff_default => [] do
  sh "vimdo dirdiff #{powerline_src}/powerline/config_files config"
end


config_files = FileList["config/**/*.json"]
powerline_config_path = File.expand_path('~/.config/powerline')

config_files.each do |f|
  distribute :FileItem do
    from f
    to   "#{f.pathmap("%{^config,#{powerline_config_path}}p")}"
    diff { |dest, src|
      system %Q{vimdo diff "#{dest}" "#{src}"}
    }
  end
end


desc "show config files"
task :config_files do
  puts config_files
end




desc "version"
task :version => [] do
  puts version
end




desc "zip for distribution"
task :zip => [] do
  sh "zip -r #{project_name}-#{version}.zip autoload plugin doc README.md --exclude='*/.DS_Store'"
end

CLEAN.include('*.zip')




vimup = File.expand_path('~/Developer/Vim/Bundle/tool/vimup/vimup')
vimorg = File.expand_path('~/.apps/vimup/vim.org.yml')

namespace :vimup do
  desc "new vim.org script"
  task :new do
    sh vimup, 'new-script', project_name, vimorg
  end

  desc "updae vim.org script"
  task :release => [:zip] do
    sh vimup, 'update-script', project_name, vimorg
    task(:clean).invoke
  end

  desc "updae vim.org script detail"
  task :details do
    sh vimup, 'update-details', project_name, vimorg
  end
end

